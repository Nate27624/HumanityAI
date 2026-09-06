#!/usr/bin/env python3
"""Validate HumanityAI's ecosystem resource registry using only stdlib."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TYPES = {"dataset", "standard", "software", "platform", "organization", "research_program"}
ALLOWED_ACCESS = {"open_data", "open_source", "public_access", "mixed"}
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load(path: str):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        fail(f"cannot load {path}: {exc}")
        return None


def is_http_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    problems_doc = load("data/problems.json")
    resources_doc = load("data/resources.json")
    schema_doc = load("schema/resource.schema.json")
    if not all(isinstance(x, dict) for x in (problems_doc, resources_doc, schema_doc)):
        return 1

    problem_ids = {
        item.get("id")
        for item in problems_doc.get("problems", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    records = resources_doc.get("records")
    if not isinstance(records, list):
        fail("data/resources.json: `records` must be a list")
        records = []

    seen_ids: set[str] = set()
    seen_names: set[str] = set()
    for i, record in enumerate(records):
        where = f"data/resources.json records[{i}]"
        if not isinstance(record, dict):
            fail(f"{where}: must be an object")
            continue

        rid = record.get("id")
        if not isinstance(rid, str) or not rid.startswith("RSC") or len(rid) != 7 or not rid[3:].isdigit():
            fail(f"{where}: id must match RSC0001-style format")
        elif rid in seen_ids:
            fail(f"{where}: duplicate id {rid}")
        else:
            seen_ids.add(rid)

        name = record.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(f"{where}: requires a non-empty name")
        else:
            normalized = name.strip().casefold()
            if normalized in seen_names:
                fail(f"{where}: duplicate resource name {name!r}")
            seen_names.add(normalized)

        if record.get("resource_type") not in ALLOWED_TYPES:
            fail(f"{where}: invalid resource_type {record.get('resource_type')!r}")
        if record.get("access_model") not in ALLOWED_ACCESS:
            fail(f"{where}: invalid access_model {record.get('access_model')!r}")

        pids = record.get("problem_ids")
        if not isinstance(pids, list) or not pids:
            fail(f"{where}: requires at least one problem_id")
        else:
            if len(pids) != len(set(pids)):
                fail(f"{where}: duplicate problem_ids")
            for pid in pids:
                if pid not in problem_ids:
                    fail(f"{where}: unknown problem_id {pid!r}")

        for field in ("maintainer", "description", "relevance"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                fail(f"{where}: requires non-empty {field}")

        for field in ("url", "evidence_url"):
            if not is_http_url(record.get(field)):
                fail(f"{where}: {field} must be an http(s) URL")

        for field in ("machine_readable", "api_available"):
            if not isinstance(record.get(field), bool):
                fail(f"{where}: {field} must be boolean")

        limitations = record.get("limitations")
        if not isinstance(limitations, list) or not limitations or any(not isinstance(x, str) or not x.strip() for x in limitations):
            fail(f"{where}: requires at least one non-empty limitation")

        try:
            date.fromisoformat(record.get("last_reviewed"))
        except (TypeError, ValueError):
            fail(f"{where}: last_reviewed must be YYYY-MM-DD")

    if not records:
        fail("data/resources.json: registry must not be empty")

    for message in errors:
        print(f"ERROR: {message}")
    print(f"Resource validation complete: {len(errors)} error(s), {len(records)} resource(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
