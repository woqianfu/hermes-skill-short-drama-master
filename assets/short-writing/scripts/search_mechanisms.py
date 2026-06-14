#!/usr/bin/env python3
"""Search bundled vertical-short-drama mechanism cards."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def index_path(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser().resolve()
    return Path(__file__).resolve().parents[3] / "assets" / "short-writing" / "assets" / "mechanism-index" / "mechanisms.jsonl"


def load_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"Missing mechanism index: {path}")
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                records.append(json.loads(line))
    return records


def tokens(query: str) -> list[str]:
    base = [x for x in re.split(r"[\s,，、/|]+", query.strip()) if x]
    lexicon = [
        "霸总", "复仇", "追妻", "火葬场", "甜宠", "萌宝", "战神", "赘婿", "神豪", "家庭伦理", "真假千金",
        "开场", "第一屏", "前10集", "前3集", "留存", "追更", "打脸", "反击", "误会", "证据", "鉴定", "直播",
        "公开羞辱", "身份", "关系误判", "追悔", "认亲", "职场", "婚礼", "家宴", "病房", "董事会",
    ]
    for word in lexicon:
        if word in query and word not in base:
            base.append(word)
    return base


def text_for(record: dict[str, Any]) -> str:
    parts: list[str] = []
    for key in [
        "id", "title", "category", "topic", "audience_emotion", "opening_model", "pressure_source",
        "secret_or_evidence", "first3_hooks", "first10_model", "retention_hook", "midgame_upgrade",
        "transferable_mechanism", "must_replace", "use_for",
    ]:
        value = record.get(key)
        if isinstance(value, list):
            parts.extend(str(x) for x in value)
        elif value:
            parts.append(str(value))
    parts.extend(record.get("tags", []))
    return "\n".join(parts)


def score(record: dict[str, Any], query: str) -> float:
    haystack = text_for(record).lower()
    title_topic = " ".join([record.get("title", ""), record.get("topic", ""), record.get("category", "")]).lower()
    total = 0.0
    for token in tokens(query):
        low = token.lower()
        if not low:
            continue
        if low in title_topic:
            total += 6
        elif low in haystack:
            total += 2
    if "first10_model" in record:
        total += 0.2
    return total


def match_filter(record: dict[str, Any], field: str, expected: str | None) -> bool:
    if not expected:
        return True
    value = record.get(field, "")
    if isinstance(value, list):
        return any(expected in str(x) for x in value)
    return expected in str(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--topic")
    parser.add_argument("--emotion")
    parser.add_argument("--tag")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--index")
    args = parser.parse_args()

    records = load_records(index_path(args.index))
    results = []
    for record in records:
        if not match_filter(record, "topic", args.topic):
            continue
        if not match_filter(record, "audience_emotion", args.emotion):
            continue
        if args.tag and args.tag not in record.get("tags", []):
            continue
        current = score(record, args.query) if args.query else 1.0
        if current > 0:
            results.append((current, record))
    results.sort(key=lambda item: (-item[0], item[1]["id"]))

    payload = []
    for current, record in results[: args.top]:
        payload.append({
            "score": round(current, 2),
            "id": record["id"],
            "title": record["title"],
            "topic": record["topic"],
            "audience_emotion": record["audience_emotion"],
            "opening_model": record["opening_model"],
            "retention_hook": record["retention_hook"],
            "tags": record.get("tags", []),
            "use_for": record.get("use_for", ""),
        })

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for i, item in enumerate(payload, start=1):
            print(f"{i}. [{item['score']}] {item['title']}")
            print(f"   id: {item['id']}")
            print(f"   topic: {item['topic']} / emotion: {item['audience_emotion']}")
            print(f"   opening: {item['opening_model']}")
            print(f"   retention: {item['retention_hook']}")
            print(f"   tags: {' / '.join(item['tags'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
