#!/usr/bin/env python3
"""Deterministic structural/provenance checks for HumanityAI.

This validator intentionally uses only the Python standard library so it can run
locally and in GitHub Actions without external dependencies.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_CLAIM_TYPES = {
    "fact",
    "estimate",
    "hypothesis",
    "value_judgment",
    "proposal",
    "unknown",
}
ALLOWED_STATUSES = {
    "supported",
    "mixed",
    "disputed",
    "insufficient_evidence",
    "superseded",
}
ALLOWED_RELATIONSHIPS = {"supports", "contradicts", "qualifies", "context"}
ALLOWED_SOURCE_TYPES = {
    "primary_data",
    "peer_reviewed",
    "systematic_review",
    "official_report",
    "preprint",
    "expert_analysis",
    "news",
    "project_documentation",
    "other",
}

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def load_json(relative_path: str):
    path = ROOT / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {relative_path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {relative_path}: {exc}")
    return None


def looks_like_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_problems() -> set[str]:
    doc = load_json("data/problems.json")
    if not isinstance(doc, dict):
        return set()

    problems = doc.get("problems")
    if not isinstance(problems, list):
        fail("data/problems.json: `problems` must be a list")
        return set()

    ids: set[str] = set()
    for index, problem in enumerate(problems):
        where = f"data/problems.json problems[{index}]"
        if not isinstance(problem, dict):
            fail(f"{where}: must be an object")
            continue
        pid = problem.get("id")
        if not isinstance(pid, str) or not pid.strip():
            fail(f"{where}: missing non-empty id")
            continue
        if pid in ids:
            fail(f"{where}: duplicate problem id {pid}")
        ids.add(pid)
        if not isinstance(problem.get("name"), str) or not problem["name"].strip():
            fail(f"{where}: missing non-empty name")

    if not ids:
        warn("problem registry contains no problem IDs")
    return ids


def validate_evidence(problem_ids: set[str]) -> None:
    doc = load_json("data/evidence.json")
    if not isinstance(doc, dict):
        return

    records = doc.get("records")
    if not isinstance(records, list):
        fail("data/evidence.json: `records` must be a list")
        return

    ids: set[str] = set()
    for index, record in enumerate(records):
        where = f"data/evidence.json records[{index}]"
        if not isinstance(record, dict):
            fail(f"{where}: must be an object")
            continue

        rid = record.get("id")
        if not isinstance(rid, str) or not rid.strip():
            fail(f"{where}: missing non-empty id")
        elif rid in ids:
            fail(f"{where}: duplicate evidence id {rid}")
        else:
            ids.add(rid)

        claim = record.get("claim")
        if not isinstance(claim, str) or not claim.strip():
            fail(f"{where}: missing non-empty claim")

        if record.get("claim_type") not in ALLOWED_CLAIM_TYPES:
            fail(f"{where}: invalid claim_type {record.get('claim_type')!r}")
        if record.get("status") not in ALLOWED_STATUSES:
            fail(f"{where}: invalid status {record.get('status')!r}")

        confidence = record.get("confidence")
        if not isinstance(confidence, (int, float)) or isinstance(confidence, bool):
            fail(f"{where}: confidence must be numeric")
        elif not 0 <= confidence <= 1:
            fail(f"{where}: confidence must be between 0 and 1")

        for pid in record.get("problem_ids", []):
            if pid not in problem_ids:
                fail(f"{where}: references unknown problem id {pid!r}")

        sources = record.get("sources")
        if not isinstance(sources, list) or len(sources) == 0:
            fail(f"{where}: every evidence record requires at least one external source")
            continue

        for source_index, source in enumerate(sources):
            sw = f"{where} sources[{source_index}]"
            if not isinstance(source, dict):
                fail(f"{sw}: must be an object")
                continue
            if not looks_like_http_url(source.get("url")):
                fail(f"{sw}: invalid or missing http(s) URL")
            if source.get("source_type") not in ALLOWED_SOURCE_TYPES:
                fail(f"{sw}: invalid source_type {source.get('source_type')!r}")
            if source.get("relationship") not in ALLOWED_RELATIONSHIPS:
                fail(f"{sw}: invalid relationship {source.get('relationship')!r}")


def validate_schema_files() -> None:
    schema_dir = ROOT / "schema"
    if not schema_dir.exists():
        fail("missing schema directory")
        return
    for path in schema_dir.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON schema file {path.relative_to(ROOT)}: {exc}")
            continue
        if not isinstance(data, dict):
            fail(f"schema file {path.relative_to(ROOT)} must contain a JSON object")
        if "$schema" not in data:
            warn(f"schema file {path.relative_to(ROOT)} has no `$schema` declaration")


def validate_required_docs() -> None:
    required = [
        "README.md",
        "PRINCIPLES.md",
        "PROBLEM_MAP.md",
        "CONTRIBUTING.md",
        "AI_OPERATIONS.md",
        "EVALUATION.md",
        "ROADMAP.md",
        "agent/CHARTER.md",
        "agent/state.json",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            fail(f"missing required project document: {relative}")


def main() -> int:
    validate_required_docs()
    problem_ids = validate_problems()
    validate_evidence(problem_ids)
    validate_schema_files()

    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}")

    print(
        f"Validation complete: {len(errors)} error(s), {len(warnings)} warning(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
