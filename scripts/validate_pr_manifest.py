#!/usr/bin/env python3

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = ROOT / "agent" / "tasks.json"
TASK_RE = re.compile(r"\bAT\d{4}\b")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


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
    for section in required_sections:
        if section.casefold() not in body.casefold():
            fail(f"external PR is missing required section: {section}")

    required_labels = [
        "Task ID:",
        "Agent/model/system:",
        "Human reviewed before submission:",
        "Coordination check:",
        "Primary/authoritative sources consulted:",
        "Important contradictory, negative, or qualifying evidence:",
        "Key uncertainty / unresolved question:",
        "Validators/tests run:",
        "Expected benefit:",
        "Plausible failure modes / ways this could be misleading:",
        "Reversibility:",
    ]
    lowered = body.casefold()
    for label in required_labels:
        if label.casefold() not in lowered:
            fail(f"external PR is missing required manifest field: {label}")

    placeholder_fragments = [
        "<!-- model or agent framework when known -->",
        "<!-- yes / no -->",
        "<!-- linked issue checked; open prs checked; draft claim used if appropriate -->",
        "<!-- describe -->",
    ]
    for placeholder in placeholder_fragments:
        if placeholder.casefold() in lowered:
            fail("external PR still contains unfilled contribution-template placeholders")

    tasks = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
    valid_task_ids = {row["id"] for row in tasks.get("tasks", []) if isinstance(row, dict) and isinstance(row.get("id"), str)}
    found_ids = set(TASK_RE.findall(body))

    if found_ids:
        unknown = sorted(found_ids - valid_task_ids)
        if unknown:
            fail(f"external PR references unknown HumanityAI task IDs: {', '.join(unknown)}")
    elif "unscheduled" not in lowered:
        fail("external PR must identify an AT#### task ID or explicitly mark the contribution unscheduled")

    checklist_items = [
        "This contribution does not treat AI-generated text as independent evidence.",
        "Consequential factual claims are traceable to verifiable sources where reasonably possible.",
        "Credible disagreement, limitations, and uncertainty are preserved.",
        "This does not weaken tests/provenance merely to obtain green CI.",
        "This does not expand autonomous authority over consequential real-world actions.",
        "I checked for materially duplicate work.",
    ]
    for item in checklist_items:
        pattern = re.compile(r"-\s*\[[xX]\]\s*" + re.escape(item))
        if not pattern.search(body):
            fail(f"external PR must affirm governance checklist item: {item}")

    print("OK: external PR contribution manifest is reviewable")


if __name__ == "__main__":
    main()
