#!/usr/bin/env python3

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "security" / "policy.json"


def fail(message: str, code: int = 1) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(code)


def load_policy() -> dict:
    try:
        policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail("missing security/policy.json")
    except json.JSONDecodeError as exc:
        fail(f"invalid security/policy.json: {exc}")

    if policy.get("schema_version") != "1.0":
        fail("security policy schema_version must be 1.0")
    if policy.get("external_content_trust") != "untrusted_data_only":
        fail("external content must remain classified as untrusted_data_only")
    if policy.get("external_pr_merge_policy") != "human_only_until_mechanical_identity_separation":
        fail("external PR merge policy must remain human-only until mechanical identity separation exists")
    if policy.get("email_on_human_review_required") is not True:
        fail("security policy must require email notification when human review is needed")

    protected = policy.get("protected_paths")
    if not isinstance(protected, list) or not protected or any(not isinstance(p, str) or not p.strip() for p in protected):
        fail("protected_paths must be a non-empty list of strings")
    return policy


def path_is_protected(path: str, protected_paths: list[str]) -> bool:
    normalized = path.strip().lstrip("./")
    for rule in protected_paths:
        rule = rule.strip().lstrip("./")
        if rule.endswith("/"):
            if normalized.startswith(rule):
                return True
        elif normalized == rule:
            return True
    return False


def main() -> None:
    policy = load_policy()

    # GitHub reserves several GITHUB_* variables, so structure-only validation uses
    # a separate explicit mode rather than attempting to override GITHUB_EVENT_NAME.
    if os.environ.get("SECURITY_STRUCTURE_ONLY", "") == "1":
        print("OK: security policy structure validated")
        return

    event = os.environ.get("GITHUB_EVENT_NAME", "")
    if event != "pull_request":
        print("OK: security policy structure validated; PR-specific human-review gate not applicable")
        return

    base_repo = os.environ.get("BASE_REPO", "").strip()
    head_repo = os.environ.get("HEAD_REPO", "").strip()
    changed_files = [p for p in (os.environ.get("CHANGED_FILES", "") or "").splitlines() if p.strip()]

    if not changed_files:
        fail("pull-request security gate received no changed-file list")

    protected_hits = [p for p in changed_files if path_is_protected(p, policy["protected_paths"])]
    external = bool(base_repo and head_repo and base_repo.casefold() != head_repo.casefold())

    reasons: list[str] = []
    if external:
        reasons.append("external_pull_request")
    if protected_hits:
        reasons.append("protected_path_change")

    if reasons:
        print("HUMAN_REVIEW_REQUIRED")
        print("reasons=" + ",".join(reasons))
        if protected_hits:
            print("protected_files=" + ",".join(protected_hits))
        print("Do not autonomously merge this PR. Preserve the exact head SHA and notify the configured human reviewer by email.")
        raise SystemExit(2)

    print(f"OK: security boundary gate passed for {len(changed_files)} changed file(s)")


if __name__ == "__main__":
    main()
