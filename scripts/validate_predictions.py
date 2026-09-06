#!/usr/bin/env python3
"""Validate pre-registered HumanityAI prediction records."""
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
errors = []


def valid_url(value):
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def fail(message):
    errors.append(message)


problems = json.loads((ROOT / "data/problems.json").read_text(encoding="utf-8"))
problem_ids = {item["id"] for item in problems["problems"]}
doc = json.loads((ROOT / "data/predictions.json").read_text(encoding="utf-8"))
records = doc.get("records")
if not isinstance(records, list):
    fail("data/predictions.json: records must be a list")
    records = []

seen = set()
for index, record in enumerate(records):
    where = f"records[{index}]"
    rid = record.get("id")
    if not isinstance(rid, str) or len(rid) != 6 or not rid.startswith("PR") or not rid[2:].isdigit():
        fail(f"{where}: id must match PR0001 format")
    elif rid in seen:
        fail(f"{where}: duplicate id {rid}")
    else:
        seen.add(rid)

    if not isinstance(record.get("question"), str) or len(record["question"].strip()) < 10:
        fail(f"{where}: question is too short")
    if not isinstance(record.get("resolution_criteria"), str) or len(record["resolution_criteria"].strip()) < 20:
        fail(f"{where}: resolution_criteria must be explicit")

    try:
        created = date.fromisoformat(record.get("created_at"))
        resolve_by = date.fromisoformat(record.get("resolve_by"))
        if resolve_by <= created:
            fail(f"{where}: resolve_by must be after created_at")
    except (TypeError, ValueError):
        fail(f"{where}: created_at and resolve_by must be ISO dates")

    probability = record.get("probability")
    if not isinstance(probability, (int, float)) or isinstance(probability, bool) or not 0.01 <= probability <= 0.99:
        fail(f"{where}: probability must be between 0.01 and 0.99")

    status = record.get("status")
    if status not in {"open", "resolved_true", "resolved_false", "invalidated"}:
        fail(f"{where}: invalid status {status!r}")

    pids = record.get("problem_ids")
    if not isinstance(pids, list) or not pids:
        fail(f"{where}: at least one problem_id is required")
    else:
        for pid in pids:
            if pid not in problem_ids:
                fail(f"{where}: unknown problem_id {pid}")

    basis = record.get("evidence_basis")
    if not isinstance(basis, list) or not basis or any(not valid_url(url) for url in basis):
        fail(f"{where}: evidence_basis requires at least one http(s) source")

    if status in {"resolved_true", "resolved_false"}:
        if not isinstance(record.get("resolution"), bool):
            fail(f"{where}: resolved prediction requires boolean resolution")
        try:
            date.fromisoformat(record.get("resolved_at"))
        except (TypeError, ValueError):
            fail(f"{where}: resolved prediction requires resolved_at ISO date")
        urls = record.get("resolution_source_urls")
        if not isinstance(urls, list) or not urls or any(not valid_url(url) for url in urls):
            fail(f"{where}: resolved prediction requires resolution_source_urls")

for error in errors:
    print(f"ERROR: {error}")
print(f"Prediction validation complete: {len(errors)} error(s), {len(records)} record(s).")
sys.exit(1 if errors else 0)
