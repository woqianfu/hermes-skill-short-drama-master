#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from typing import Any

from library_common import LIBRARY_DIR, infer_profile, load_jsonl, tokens


def text_for(record: dict[str, Any]) -> str:
    parts: list[str] = []
    for key in [
        "id", "title", "category", "audience_emotion", "type_promise", "opening_pressure",
        "first3_model", "first10_model", "midgame_upgrade", "evidence_or_secret",
        "opening_scene_options", "transferable_mechanism", "use_for", "tags",
    ]:
        value = record.get(key)
        if isinstance(value, list):
            parts.extend(str(x) for x in value)
        elif value:
            parts.append(str(value))
    return "\n".join(parts).lower()


def score(record: dict[str, Any], query: str) -> float:
    haystack = text_for(record)
    head = " ".join([record.get("title", ""), record.get("category", ""), record.get("audience_emotion", "")]).lower()
    total = 0.0
    _, profile = infer_profile(record.get("category", ""), record.get("title", ""))
    if any(alias and alias in query for alias in profile.get("aliases", [])):
        total += 6
    for token in tokens(query):
        low = token.lower()
        if low in head:
            total += 7
        elif low in haystack:
            total += 2
    if "前10" in query and record.get("first10_model"):
        total += 1
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description="Search portable distilled short-drama case cards.")
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--category")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--library", default=str(LIBRARY_DIR / "case_cards.jsonl"))
    args = parser.parse_args()

    records = load_jsonl(__import__("pathlib").Path(args.library))
    results: list[tuple[float, dict[str, Any]]] = []
    for record in records:
        if args.category and args.category not in record.get("category", ""):
            continue
        current = score(record, args.query) if args.query else 1.0
        if current > 0:
            results.append((current, record))
    results.sort(key=lambda item: (-item[0], item[1].get("id", "")))

    payload = []
    for current, record in results[: args.top]:
        payload.append({
            "score": round(current, 2),
            "id": record["id"],
            "title": record["title"],
            "category": record["category"],
            "audience_emotion": record["audience_emotion"],
            "opening": record["opening_pressure"],
            "first10_model": record["first10_model"],
            "midgame_upgrade": record["midgame_upgrade"],
            "tags": record.get("tags", []),
        })

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for idx, item in enumerate(payload, start=1):
            print(f"{idx}. [{item['score']}] {item['title']}")
            print(f"   id: {item['id']}")
            print(f"   category: {item['category']} / emotion: {item['audience_emotion']}")
            print(f"   opening: {item['opening']}")
            print(f"   first10: {item['first10_model']}")
            print(f"   upgrade: {item['midgame_upgrade']}")
            print(f"   tags: {' / '.join(item['tags'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
