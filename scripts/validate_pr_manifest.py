#!/usr/bin/env python3

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = ROOT / "agent" / "tasks.json"
TASK_RE = re.compile(r"^AT\d{4}$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def extract_field(body: str, label: str) -> str:
    pattern = re.compile(rf"\*\*{re.escape(label)}:\*\*\s*(.*)", re.IGNORECASE)
    match = pattern.search(body)
    if not match:
        fail(f"external PR is missing required manifest field: {label}:")
    value = match.group(1).strip()
    if not value or value.startswith("<!--"):
        fail(f"external PR has an unfilled manifest field: {label}:")
    return value


def main() -> None:
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    if event != "pull_request":
        print("OK: PR manifest validation not applicable to this event")
        return

    base_repo = os.environ.get("BASE_REPO", "").strip()
    head_repo = os.environ.get("HEAD_REPO", "").strip()
    body = os.environ.get("PR_BODY", "") or ""

    # Same-repository maintainer PRs are already governed by the internal agent/human
    # workflow. External forks get the strict donated-compute manifest gate.
    if head_repo and base_repo and head_repo.casefold() == base_repo.casefold():
        print("OK: same-repository PR; external-agent manifest gate not required")
        return

    if len(body.strip()) < 250:
        fail("external PR body is too short to provide a reviewable contribution manifest")

    required_sections = [
        "### Contribution manifest",
        "### Evidence and epistemics",
        "### Evaluation",
        "### Files changed",
        "### Governance and safety checklist",
    ]
    lowered = body.casefold()
    for section in required_sections:
        if section.casefold() not in lowered:
            fail(f"external PR is missing required section: {section}")

    task_value = extract_field(body, "Task ID")
    extract_field(body, "Agent/model/system")
    human_review = extract_field(body, "Human reviewed before submission").casefold()
    extract_field(body, "Coordination check")

    if human_review not in {"yes", "no"}:
        fail("Human reviewed before submission must be exactly yes or no")

    required_text_labels = [
        "Primary/authoritative sources consulted",
        "Important contradictory, negative, or qualifying evidence",
        "Key uncertainty / unresolved question",
        "Validators/tests run",
        "Expected benefit",
        "Plausible failure modes / ways this could be misleading",
        "Reversibility",
    ]
    for label in required_text_labels:
        if f"**{label}:**".casefold() not in lowered:
            fail(f"external PR is missing required manifest field: {label}:")

    tasks = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
    valid_task_ids = {row["id"] for row in tasks.get("tasks", []) if isinstance(row, dict) and isinstance(row.get("id"), str)}

    task_token = re.sub(r"[`*_]", "", task_value).strip()
    if task_token.casefold().startswith("unscheduled"):
        justification = task_token[len("unscheduled"):].strip(" :-—")
        if len(justification) < 15:
            fail("unscheduled external PRs must justify why the work is not in agent/tasks.json")
    else:
        token = task_token.split()[0] if task_token else ""
        if not TASK_RE.fullmatch(token):
            fail("external PR Task ID must be an AT#### identifier or 'unscheduled' with justification")
        if token not in valid_task_ids:
            fail(f"external PR references unknown HumanityAI task ID: {token}")

    checklist_items = [
        "This contribution does not treat AI-generated text as independent evidence.",
        "Consequential factual claims are traceable to verifiable sources where reasonably possible.",
        "Credible disagreement, limitations, and uncertainty are preserved.",
        "This does not weaken tests/provenance merely to obtain green CI.",
        "This does not expand autonomous authority over consequential real-world actions.",
        "This does not silently modify foundational human-agency, rights, consent, pluralism, peaceful-cooperation, or governance protections.",
        "I checked for materially duplicate work.",
        "I have the right to submit my contribution under the repository's Apache-2.0 license and have not silently relicensed third-party source material.",
    ]
    for item in checklist_items:
        pattern = re.compile(r"-\s*\[[xX]\]\s*" + re.escape(item))
        if not pattern.search(body):
            fail(f"external PR must affirm governance checklist item: {item}")

    print("OK: external PR contribution manifest is reviewable")


if __name__ == "__main__":
    main()
