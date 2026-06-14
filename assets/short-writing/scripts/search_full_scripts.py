#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Any

from library_common import (
    FULL_SCRIPT_CIPHER,
    FULL_SCRIPT_ITERATIONS,
    FULL_SCRIPT_KEY_ENV,
    FULL_SCRIPTS_DIR,
    LOCAL_FULL_LIBRARY,
    full_script_key,
    full_script_key_source,
    norm,
    read_body,
    tokens,
)


def score_text(title: str, category: str, body: str, query: str) -> float:
    text = f"{title}\n{category}\n{body}".lower()
    total = 0.0
    for token in tokens(query):
        low = token.lower()
        if low in title.lower() or low in category.lower():
            total += 8
        elif low in text:
            total += 2
    if norm(query) and norm(query) in norm(title):
        total += 10
    return total


def score_file(path: Path, query: str, root: Path) -> tuple[float, dict[str, Any]]:
    rel = path.relative_to(root)
    title = path.stem
    category = rel.parts[0].replace("_", "/") if len(rel.parts) > 1 else "未分类"
    total = score_text(title, category, read_body(path, 4000), query)
    return total, {"title": title, "category": category, "path": str(path), "chars": len(read_body(path))}


def load_manifest(source: Path) -> list[dict[str, Any]]:
    manifest = source / "manifest.jsonl"
    if not manifest.exists():
        return []
    rows: list[dict[str, Any]] = []
    with manifest.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def decrypt_preview(source: Path, filename: str, limit: int = 4000) -> str:
    key = full_script_key()
    if not key:
        return ""
    env = os.environ.copy()
    env[FULL_SCRIPT_KEY_ENV] = key
    completed = subprocess.run(
        [
            "openssl", "enc", "-d", f"-{FULL_SCRIPT_CIPHER}", "-pbkdf2", "-iter", FULL_SCRIPT_ITERATIONS,
            "-md", "sha256", "-in", str(source / filename), "-pass", f"env:{FULL_SCRIPT_KEY_ENV}",
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    text = completed.stdout.decode("utf-8", errors="ignore")
    if "## 正文" in text:
        text = text.split("## 正文", 1)[1]
    return text[:limit]


def search_encrypted_source(source: Path, query: str, top: int) -> None:
    rows = load_manifest(source)
    key = full_script_key()
    has_key = bool(key)
    key_source = full_script_key_source() if has_key else "none"
    results = []
    for row in rows:
        body = ""
        body_search = False
        if has_key:
            try:
                body = decrypt_preview(source, row["filename"])
                body_search = True
            except subprocess.CalledProcessError:
                body = ""
        current = score_text(row.get("title", ""), row.get("category", ""), body, query)
        if current > 0 or not query:
            results.append((current if query else 1.0, {
                "title": row.get("title", ""),
                "category": row.get("category", ""),
                "path": str(source / row["filename"]),
                "chars": row.get("chars", 0),
                "encrypted": True,
                "body_search": body_search,
            }))
    results.sort(key=lambda item: (-item[0], item[1]["title"]))
    print(f"skill 内置完整剧本库: {source}")
    if has_key:
        key_label = "内置密钥" if key_source == "builtin" else f"环境变量 {FULL_SCRIPT_KEY_ENV}"
        print(f"正文检索: yes / key_source: {key_source} / {key_label}")
    else:
        print(f"未设置 {FULL_SCRIPT_KEY_ENV}，仅按 manifest 的剧名和分类检索；设置密钥后可检索正文。")
    for idx, (current, item) in enumerate(results[:top], start=1):
        print(f"{idx}. [{round(current, 2)}] {item['title']}")
        print(f"   category: {item['category']}")
        print(f"   chars: {item['chars']}")
        print(f"   encrypted: yes / body_search: {'yes' if item['body_search'] else 'no'}")
        print(f"   path: {item['path']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Search bundled encrypted full scripts first, then local private corpus.")
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--source")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--local-only", action="store_true")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve() if args.source else FULL_SCRIPTS_DIR
    if source.exists() and (source / "manifest.jsonl").exists():
        search_encrypted_source(source, args.query, args.top)
        return 0

    if not args.source:
        source = LOCAL_FULL_LIBRARY
    source = source.expanduser().resolve()
    if not source.exists():
        print(f"未找到本机完整库: {source}")
        print("分享版仍可使用 assets/library 蒸馏库。")
        return 0

    results = []
    for path in source.rglob("*.md"):
        if path.name in {"索引.md"}:
            continue
        current, meta = score_file(path, args.query, source)
        if current > 0 or not args.query:
            results.append((current if args.query else 1.0, meta))
    results.sort(key=lambda item: (-item[0], item[1]["title"]))

    print(f"本机完整库: {source}")
    for idx, (current, item) in enumerate(results[: args.top], start=1):
        print(f"{idx}. [{round(current, 2)}] {item['title']}")
        print(f"   category: {item['category']}")
        print(f"   chars: {item['chars']}")
        print(f"   path: {item['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
