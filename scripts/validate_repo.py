#!/usr/bin/env python3
"""Deterministic structural/provenance checks for HumanityAI.

This validator intentionally uses only the Python standard library so it can run
locally and in GitHub Actions without external dependencies.
"""

from __future__ import annotations

import json
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_CLAIM_TYPES = {"fact", "estimate", "hypothesis", "value_judgment", "proposal", "unknown"}
ALLOWED_STATUSES = {"supported", "mixed", "disputed", "insufficient_evidence", "superseded"}
ALLOWED_RELATIONSHIPS = {"supports", "contradicts", "qualifies", "context"}
ALLOWED_SOURCE_TYPES = {"primary_data", "peer_reviewed", "systematic_review", "official_report", "preprint", "expert_analysis", "news", "project_documentation", "other"}
ALLOWED_INDICATOR_VALUE_TYPES = {"observed", "estimate", "projection", "index"}
ALLOWED_INDICATOR_SOURCE_TYPES = {"primary_data", "official_report", "peer_reviewed", "systematic_review"}
ALLOWED_HEARTBEAT_STATUSES = {
    "not_yet_recorded",
    "success",
    "partial_success",
    "no_change_needed",
    "blocked_transient",
    "blocked_permission",
    "blocked_governance",
    "failed_validation",
    "reverted",
}
EXPECTED_HEARTBEATS = {
    "primary": 26,
    "frontier": 41,
    "secondary": 56,
    "audit": 11,
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


def is_iso_datetime(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


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


def validate_indicators(problem_ids: set[str]) -> None:
    doc = load_json("data/indicators.json")
    if not isinstance(doc, dict):
        return
    records = doc.get("records")
    if not isinstance(records, list):
        fail("data/indicators.json: `records` must be a list")
        return
    ids: set[str] = set()
    for index, record in enumerate(records):
        where = f"data/indicators.json records[{index}]"
        if not isinstance(record, dict):
            fail(f"{where}: must be an object")
            continue
        rid = record.get("id")
        if not isinstance(rid, str) or not rid.strip():
            fail(f"{where}: missing non-empty id")
        elif rid in ids:
            fail(f"{where}: duplicate indicator id {rid}")
        else:
            ids.add(rid)
        pids = record.get("problem_ids")
        if not isinstance(pids, list) or not pids:
            fail(f"{where}: requires at least one problem_id")
        else:
            for pid in pids:
                if pid not in problem_ids:
                    fail(f"{where}: references unknown problem id {pid!r}")
        if not isinstance(record.get("name"), str) or not record["name"].strip():
            fail(f"{where}: missing non-empty name")
        value = record.get("value")
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            fail(f"{where}: value must be numeric")
        if not isinstance(record.get("unit"), str) or not record["unit"].strip():
            fail(f"{where}: missing non-empty unit")
        if record.get("value_type") not in ALLOWED_INDICATOR_VALUE_TYPES:
            fail(f"{where}: invalid value_type {record.get('value_type')!r}")
        for field in ("reference_period", "geography"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                fail(f"{where}: missing non-empty {field}")
        limitations = record.get("limitations")
        if not isinstance(limitations, list) or not limitations or any(not isinstance(x, str) or not x.strip() for x in limitations):
            fail(f"{where}: requires at least one non-empty limitation")
        reviewed = record.get("last_reviewed")
        try:
            date.fromisoformat(reviewed)
        except (TypeError, ValueError):
            fail(f"{where}: last_reviewed must be ISO date YYYY-MM-DD")
        source = record.get("source")
        if not isinstance(source, dict):
            fail(f"{where}: missing source object")
            continue
        for field in ("publisher", "title", "published_at"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                fail(f"{where} source: missing non-empty {field}")
        if not looks_like_http_url(source.get("url")):
            fail(f"{where} source: invalid or missing http(s) URL")
        if source.get("source_type") not in ALLOWED_INDICATOR_SOURCE_TYPES:
            fail(f"{where} source: invalid source_type {source.get('source_type')!r}")


def validate_heartbeats() -> None:
    required_keys = {
        "schema_version",
        "role",
        "expected_cadence_minutes",
        "expected_minute",
        "last_attempt_at",
        "last_success_at",
        "last_status",
        "last_run_key",
        "consecutive_non_success",
        "notes",
    }
    heartbeat_dir = ROOT / "agent" / "heartbeats"
    for role, expected_minute in EXPECTED_HEARTBEATS.items():
        relative = f"agent/heartbeats/{role}.json"
        doc = load_json(relative)
        if not isinstance(doc, dict):
            continue
        where = relative
        extra = set(doc) - required_keys
        missing = required_keys - set(doc)
        if missing:
            fail(f"{where}: missing heartbeat field(s): {', '.join(sorted(missing))}")
        if extra:
            fail(f"{where}: unexpected heartbeat field(s): {', '.join(sorted(extra))}")
        if doc.get("schema_version") != "1.0":
            fail(f"{where}: schema_version must be '1.0'")
        if doc.get("role") != role:
            fail(f"{where}: role must match filename ({role})")
        if doc.get("expected_cadence_minutes") != 60:
            fail(f"{where}: expected_cadence_minutes must be 60")
        if doc.get("expected_minute") != expected_minute:
            fail(f"{where}: expected_minute must be {expected_minute} for {role}")
        status = doc.get("last_status")
        if status not in ALLOWED_HEARTBEAT_STATUSES:
            fail(f"{where}: invalid last_status {status!r}")
        counter = doc.get("consecutive_non_success")
        if not isinstance(counter, int) or isinstance(counter, bool) or counter < 0:
            fail(f"{where}: consecutive_non_success must be a non-negative integer")
        if not isinstance(doc.get("notes"), str):
            fail(f"{where}: notes must be a string")
        for field in ("last_attempt_at", "last_success_at"):
            value = doc.get(field)
            if value is not None and not is_iso_datetime(value):
                fail(f"{where}: {field} must be null or ISO date-time")
        run_key = doc.get("last_run_key")
        if run_key is not None and (not isinstance(run_key, str) or not run_key.strip()):
            fail(f"{where}: last_run_key must be null or a non-empty string")
        if status == "not_yet_recorded":
            if any(doc.get(field) is not None for field in ("last_attempt_at", "last_success_at", "last_run_key")):
                fail(f"{where}: not_yet_recorded heartbeat must have null timestamps/run key")
            if counter != 0:
                fail(f"{where}: not_yet_recorded heartbeat must have consecutive_non_success=0")
        else:
            if doc.get("last_attempt_at") is None or run_key is None:
                fail(f"{where}: recorded heartbeat requires last_attempt_at and last_run_key")
            if status in {"success", "no_change_needed"} and doc.get("last_success_at") is None:
                fail(f"{where}: successful heartbeat requires last_success_at")
            if status in {"success", "no_change_needed"} and counter != 0:
                fail(f"{where}: successful heartbeat must reset consecutive_non_success to 0")
        attempt = doc.get("last_attempt_at")
        success = doc.get("last_success_at")
        if attempt is not None and success is not None:
            attempt_dt = datetime.fromisoformat(attempt.replace("Z", "+00:00"))
            success_dt = datetime.fromisoformat(success.replace("Z", "+00:00"))
            if success_dt > attempt_dt:
                fail(f"{where}: last_success_at cannot be later than last_attempt_at")

    expected_files = {f"{role}.json" for role in EXPECTED_HEARTBEATS}
    if heartbeat_dir.exists():
        actual_json = {path.name for path in heartbeat_dir.glob("*.json")}
        unexpected = actual_json - expected_files
        if unexpected:
            fail(f"agent/heartbeats: unexpected role heartbeat file(s): {', '.join(sorted(unexpected))}")


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
    required = ["README.md", "PRINCIPLES.md", "PROBLEM_MAP.md", "CONTRIBUTING.md", "AI_OPERATIONS.md", "EVALUATION.md", "IMPACT_MODEL.md", "FAILURE_RECOVERY.md", "ROADMAP.md", "agent/CHARTER.md", "agent/state.json", "agent/heartbeats/README.md", "schema/agent-heartbeat.schema.json"]
    for relative in required:
        if not (ROOT / relative).exists():
            fail(f"missing required project document: {relative}")


def main() -> int:
    validate_required_docs()
    problem_ids = validate_problems()
    validate_evidence(problem_ids)
    validate_indicators(problem_ids)
    validate_heartbeats()
    validate_schema_files()
    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}")
    print(f"Validation complete: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
