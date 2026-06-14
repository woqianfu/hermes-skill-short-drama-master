#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from library_common import LIBRARY_DIR, load_jsonl


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect one distilled short-drama case card.")
    parser.add_argument("case_id")
    parser.add_argument("--library", default=str(LIBRARY_DIR / "case_cards.jsonl"))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    rows = load_jsonl(Path(args.library))
    card = next((row for row in rows if row.get("id") == args.case_id or row.get("script_id") == args.case_id), None)
    if not card:
        raise SystemExit(f"Missing case: {args.case_id}")

    if args.json:
        print(json.dumps(card, ensure_ascii=False, indent=2))
        return 0

    print(f"【案例】{card['title']} ({card['id']})")
    print(f"【类型】{card['category']} / {card['audience_emotion']}")
    print(f"【类型承诺】{card['type_promise']}")
    print(f"【第一屏压力】{card['opening_pressure']}")
    print(f"【前3集模型】{card['first3_model']}")
    print(f"【前10集模型】{card['first10_model']}")
    print(f"【中段升级】{card['midgame_upgrade']}")
    print(f"【可借鉴机制】{card['transferable_mechanism']}")
    print(f"【必须替换】{' / '.join(card['must_replace'])}")
    print(f"【相似风险】{card['originality_risk']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
