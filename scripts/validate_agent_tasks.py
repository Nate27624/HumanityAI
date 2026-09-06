#!/usr/bin/env python3

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = ROOT / "agent" / "tasks.json"
PROBLEMS_PATH = ROOT / "data" / "problems.json"

VALID_STATUS = {"open", "claimed", "blocked", "in_review", "complete", "retired"}
VALID_PRIORITY = {"critical", "high", "medium", "low"}
VALID_COORDINATION = {"exclusive", "parallel_ok"}
TASK_RE = re.compile(r"^AT\d{4}$")
PROBLEM_RE = re.compile(r"^P\d{2}$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def nonempty_string(value, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{field} must be a non-empty string")
    return value.strip()


def valid_http_url(value: str, field: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(f"{field} must be an absolute http(s) URL")


def valid_datetime(value: str, field: str) -> None:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        fail(f"{field} must be ISO-8601 date-time")


def valid_date(value: str, field: str) -> None:
    try:
        date.fromisoformat(value)
    except Exception:
        fail(f"{field} must be ISO-8601 date")


def validate_string_list(value, field: str, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list):
        fail(f"{field} must be an array")
    if not allow_empty and not value:
        fail(f"{field} must not be empty")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        fail(f"{field} must contain only non-empty strings")
    if len(value) != len(set(value)):
        fail(f"{field} must not contain duplicates")
    return value


def main() -> None:
    payload = load_json(TASKS_PATH)
    problems = load_json(PROBLEMS_PATH)

    if payload.get("schema_version") != "1.0":
        fail("agent/tasks.json schema_version must be 1.0")

    updated_at = nonempty_string(payload.get("updated_at"), "updated_at")
    valid_datetime(updated_at, "updated_at")

    claim_policy = payload.get("claim_policy")
    if not isinstance(claim_policy, dict):
        fail("claim_policy must be an object")
    hours = claim_policy.get("default_claim_hours")
    if not isinstance(hours, int) or not 1 <= hours <= 168:
        fail("claim_policy.default_claim_hours must be an integer from 1 to 168")
    instructions = nonempty_string(claim_policy.get("instructions"), "claim_policy.instructions")
    if len(instructions) < 20:
        fail("claim_policy.instructions is too short")

    valid_problem_ids = set()
    problem_rows = problems.get("problems", problems) if isinstance(problems, dict) else problems
    if isinstance(problem_rows, list):
        for row in problem_rows:
            if isinstance(row, dict) and isinstance(row.get("id"), str):
                valid_problem_ids.add(row["id"])
    if not valid_problem_ids:
        fail("could not load valid problem IDs from data/problems.json")

    tasks = payload.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        fail("tasks must be a non-empty array")

    ids: set[str] = set()
    titles: set[str] = set()

    for index, task in enumerate(tasks):
        prefix = f"tasks[{index}]"
        if not isinstance(task, dict):
            fail(f"{prefix} must be an object")

        task_id = nonempty_string(task.get("id"), f"{prefix}.id")
        if not TASK_RE.fullmatch(task_id):
            fail(f"{prefix}.id must match AT0000 format")
        if task_id in ids:
            fail(f"duplicate task id: {task_id}")
        ids.add(task_id)

        title = nonempty_string(task.get("title"), f"{prefix}.title")
        normalized_title = title.casefold()
        if normalized_title in titles:
            fail(f"duplicate task title: {title}")
        titles.add(normalized_title)

        if task.get("status") not in VALID_STATUS:
            fail(f"{prefix}.status is invalid")
        if not isinstance(task.get("agent_ready"), bool):
            fail(f"{prefix}.agent_ready must be boolean")
        if task.get("priority") not in VALID_PRIORITY:
            fail(f"{prefix}.priority is invalid")
        if task.get("coordination_mode") not in VALID_COORDINATION:
            fail(f"{prefix}.coordination_mode is invalid")

        validate_string_list(task.get("skills"), f"{prefix}.skills")
        problem_ids = validate_string_list(task.get("problem_ids"), f"{prefix}.problem_ids", allow_empty=True)
        for problem_id in problem_ids:
            if not PROBLEM_RE.fullmatch(problem_id) or problem_id not in valid_problem_ids:
                fail(f"{prefix}.problem_ids contains unknown id {problem_id}")

        for field in ("objective", "why_it_matters"):
            text = nonempty_string(task.get(field), f"{prefix}.{field}")
            if len(text) < 20:
                fail(f"{prefix}.{field} is too short")

        validate_string_list(task.get("completion_criteria"), f"{prefix}.completion_criteria")
        validate_string_list(task.get("allowed_changes"), f"{prefix}.allowed_changes")
        validate_string_list(task.get("evidence_requirements"), f"{prefix}.evidence_requirements")

        blocked_by = validate_string_list(task.get("blocked_by"), f"{prefix}.blocked_by", allow_empty=True)
        if task_id in blocked_by:
            fail(f"{prefix}.blocked_by cannot reference itself")

        issue_url = task.get("issue_url")
        if issue_url is not None:
            nonempty_string(issue_url, f"{prefix}.issue_url")
            valid_http_url(issue_url, f"{prefix}.issue_url")

        claimed_by = task.get("claimed_by")
        claim_expires = task.get("claim_expires_at")
        if claimed_by is not None:
            nonempty_string(claimed_by, f"{prefix}.claimed_by")
        if claim_expires is not None:
            valid_datetime(nonempty_string(claim_expires, f"{prefix}.claim_expires_at"), f"{prefix}.claim_expires_at")

        if task.get("status") == "claimed":
            if not claimed_by or not claim_expires:
                fail(f"{prefix}: claimed tasks require claimed_by and claim_expires_at")
        elif claimed_by is not None or claim_expires is not None:
            fail(f"{prefix}: claim fields should be null unless status is claimed")

        last_reviewed = nonempty_string(task.get("last_reviewed"), f"{prefix}.last_reviewed")
        valid_date(last_reviewed, f"{prefix}.last_reviewed")

    for index, task in enumerate(tasks):
        for blocker in task["blocked_by"]:
            if blocker not in ids:
                fail(f"tasks[{index}].blocked_by references unknown task {blocker}")

    print(f"OK: validated {len(tasks)} external-agent tasks")


if __name__ == "__main__":
    main()
