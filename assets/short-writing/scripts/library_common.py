#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[3]
LIBRARY_DIR = SKILL_ROOT / "assets" / "short-writing" / "library"
FULL_SCRIPTS_DIR = SKILL_ROOT / "assets" / "short-writing" / "full-scripts"
LOCAL_FULL_LIBRARY = Path("/Volumes/project/短剧资料/全部剧本_统一Markdown_去重分类")
FULL_SCRIPT_KEY_ENV = "VSDW_FULL_SCRIPT_KEY"
FULL_SCRIPT_CIPHER = "aes-256-cbc"
FULL_SCRIPT_ITERATIONS = "20000"
_BUILTIN_FULL_SCRIPT_KEY_PARTS = [
    "vsdw-full-script-library",
    "::private-obfuscation",
    "::2026-06-02",
    "::do-not-use-for-strong-secrecy",
]


def builtin_full_script_key() -> str:
    return "".join(_BUILTIN_FULL_SCRIPT_KEY_PARTS)


def full_script_key() -> str:
    return os.environ.get(FULL_SCRIPT_KEY_ENV) or builtin_full_script_key()


def full_script_key_source() -> str:
    return "env" if os.environ.get(FULL_SCRIPT_KEY_ENV) else "builtin"


TYPE_PROFILES: dict[str, dict[str, Any]] = {
    "女频短剧/霸总": {
        "aliases": ["霸总", "豪门", "总裁", "傅总", "顾总", "裴总", "闪婚", "财阀"],
        "emotion": "权力差误判后的偏爱和公开选择",
        "promise": "强权关系里先误判压迫，再用选择、身份或资源反转。",
        "opening": "女主在婚姻、职场或豪门场被公开误判，权力方站错队。",
        "first3": "1公开压迫，2权力方继续误判，3女主拿到小证据或小资源。",
        "first10": "1-3压迫误判，4-6反派补刀，7-9女主局部反击，10权力方发现异常。",
        "midgame": "从情感误会升级到家族、公司、舆论和财产规则。",
        "pitfalls": ["只有命令和宠爱", "女主没有低位压力", "反击工具不具体"],
    },
    "女频短剧/追妻火葬场": {
        "aliases": ["追妻", "火葬场", "前妻", "离婚", "前夫", "余情未了"],
        "emotion": "错爱追悔和行动补偿",
        "promise": "伤害者迟来追悔，受伤者离开并重新掌握选择权。",
        "opening": "亲密关系对象当众误判主角，造成可见且不可逆的伤害。",
        "first3": "1伤害成立，2证据受阻，3主角离开或第一次反击。",
        "first10": "前3集制造具体伤害，4-7集离场反噬，8-10集真相露角但补偿失败。",
        "midgame": "从道歉升级为公开站队、资源补偿、旧伤清算。",
        "pitfalls": ["伤害不具体", "追悔只靠哭", "主角长期无行动"],
    },
    "女频短剧/重生复仇": {
        "aliases": ["复仇", "重生", "真千金", "假千金", "逆袭", "渣男", "归来"],
        "emotion": "被害者带证据逐层清算",
        "promise": "主角从低位回到局中，用未来信息、旧证据或新资源逐个清算。",
        "opening": "旧伤或当下羞辱先被看见，主角在关键选择上不再重蹈覆辙。",
        "first3": "1旧伤/羞辱，2主角改写选择，3小反派第一次失算。",
        "first10": "每2-3集清算一个小伤害，第10集抬出幕后或更大旧账。",
        "midgame": "复仇对象从贴身小反派升级到资源控制者和关系背叛者。",
        "pitfalls": ["主角过早碾压", "只有打脸没有旧债", "反派太蠢"],
    },
    "女频短剧/甜宠": {
        "aliases": ["甜宠", "恋爱", "娇养", "心动", "罗曼史", "腹黑女佣"],
        "emotion": "强绑定关系里的亲密推进",
        "promise": "甜点和阻碍轮换，让关系从假绑定到公开偏爱。",
        "opening": "闪婚、契约、救助、同居或误会把两人强行绑在一起。",
        "first3": "1绑定，2误会或外敌打断，3第一次偏爱露出。",
        "first10": "每集一个亲密推进，但被身份差、旧账或外敌持续打断。",
        "midgame": "从私下心动升级到公开偏爱和共同对抗。",
        "pitfalls": ["只有甜没有阻碍", "没有下一集问题", "外敌不推动关系"],
    },
    "女频短剧/萌宝": {
        "aliases": ["萌宝", "妈咪", "爹地", "孩子", "孕检单", "父凭子贵", "多宝"],
        "emotion": "孩子作为线索和关系债",
        "promise": "孩子推动认亲、补偿、站队和旧伤揭开。",
        "opening": "孩子制造相遇、危机或误会，让亲子秘密变成第一屏钩子。",
        "first3": "1孩子出场制造危机，2亲子线索被误读，3孩子递出关键小证据。",
        "first10": "孩子递线索、拆谎、制造亲密，每3集逼近一次身份确认。",
        "midgame": "从认亲升级为抚养权、鉴定真假和家族站队。",
        "pitfalls": ["孩子只卖萌", "鉴定一次解决", "亲子线不推动主线"],
    },
    "女频短剧/虐恋": {
        "aliases": ["虐恋", "错爱", "噬骨", "伤痕", "潜逃", "撕夜"],
        "emotion": "深误会后的情绪清算",
        "promise": "深伤害先成立，真相迟到，但主角必须逐步拿回选择权。",
        "opening": "亲密关系把主角逼到绝境，误判有证据、场面和旁人站队。",
        "first3": "1绝境伤害，2真相缺页，3主角自救或留下一枚证据。",
        "first10": "真相每集露一点但无法完整公开，压迫和反击交替。",
        "midgame": "虐点转向清算、补偿和主角重新选择。",
        "pitfalls": ["虐而不爽", "误会只靠不说话", "主角无行动"],
    },
    "男频短剧/战神": {
        "aliases": ["战神", "武神", "战尊", "镇狱", "北王", "强者"],
        "emotion": "强者被低估后的层层释放",
        "promise": "隐藏强者从低位受辱开始，逐层释放能力、旧部和身份。",
        "opening": "主角以低位身份被公开羞辱，强者身份只露一角。",
        "first3": "1受辱，2小试能力，3更高权力第一次试探。",
        "first10": "身份释放分层：能力、资源、旧部、称号、终局审判。",
        "midgame": "从局部打脸升级到权力系统和旧敌清算。",
        "pitfalls": ["第一集直接无敌", "没有更高压迫者", "只打脸不救人"],
    },
    "男频短剧/赘婿": {
        "aliases": ["赘婿", "上门", "女婿", "岳母", "妻族"],
        "emotion": "家庭低位者逆袭并改变站队",
        "promise": "低位赘婿用隐藏能力、资源和担当改变家庭站队。",
        "opening": "饭桌、婚礼或公司会议里主角被妻族公开羞辱。",
        "first3": "1羞辱，2危机出现，3主角解决一件事但不完全暴露。",
        "first10": "主角边忍边救场，妻子站队逐步变化，外部敌人抬高压力。",
        "midgame": "从家庭羞辱升级到公司资源、家族权力和外部敌人。",
        "pitfalls": ["只有打脸", "妻子站队不清楚", "关系债不足"],
    },
    "男频短剧/神豪": {
        "aliases": ["神豪", "首富", "财富", "财神", "美女总裁"],
        "emotion": "金钱羞辱后的财富反差",
        "promise": "主角被当成穷人或骗子，资源真相持续反转。",
        "opening": "现场出现必须用资源解决的危机，主角被低估。",
        "first3": "1被羞辱，2小额资源反打，3更大资源线索露出。",
        "first10": "每2-3集释放一个更高资源，保留真实财富来源谜底。",
        "midgame": "从花钱打脸转向资源调度、商业权力和关系审判。",
        "pitfalls": ["只堆金额", "没有现实危机", "关系误判不足"],
    },
    "男频短剧/修仙": {
        "aliases": ["修仙", "神仙", "玄幻", "灵异", "妖", "神算", "转生"],
        "emotion": "超常能力进入现实压迫",
        "promise": "超常能力先解决现实危机，再引出更大规则和敌人。",
        "opening": "主角能力被低估或误解，现实羞辱逼出第一层能力。",
        "first3": "1现实压迫，2能力小显，3规则或敌人反噬。",
        "first10": "能力释放必须换来更高规则压力，而不是一路碾压。",
        "midgame": "从个人能力升级到门派、家族、城市或规则系统。",
        "pitfalls": ["能力无代价", "规则不清", "现实情绪太弱"],
    },
    "家庭向/年代家庭": {
        "aliases": ["家庭", "年代", "八零", "70年代", "后妈", "婆婆"],
        "emotion": "家人误判、生活压迫和家庭站队",
        "promise": "主角在家庭规则里被压低，再用生活能力和证据改变站队。",
        "opening": "饭桌、邻里或家族场景里，主角被公开定罪或排斥。",
        "first3": "1家庭审判，2生活危机，3主角用规则或能力反打一口。",
        "first10": "家人站队反复，外部生活压力和内部旧账交替推进。",
        "midgame": "从家务冲突升级到财产、孩子、名誉和旧案。",
        "pitfalls": ["只吵架", "没有生活事件", "站队不变化"],
    },
    "古装短剧/古装权谋": {
        "aliases": ["古装", "古代", "太子", "长公主", "皇后", "女帝", "宫女"],
        "emotion": "身份等级压迫下的规则反用",
        "promise": "主角在等级和礼法中被压迫，再借规则、身份或证据反击。",
        "opening": "朝堂、后宅、婚宴或刑罚场里，主角被公开审判。",
        "first3": "1公开审判，2证据/身份受阻，3主角反用规则小胜。",
        "first10": "每次反击都引出更高等级裁判和更重代价。",
        "midgame": "从后宅争斗升级到朝堂、兵权、继承或天下规则。",
        "pitfalls": ["只换古装皮", "礼法规则不推动剧情", "反派无权力"],
    },
    "悬疑短剧": {
        "aliases": ["悬疑", "消失", "救赎", "危机", "迷踪", "七宗罪"],
        "emotion": "真相碎片和误判反转",
        "promise": "用证据碎片让观众不断改判，真相每次接近又被推翻。",
        "opening": "一个异常事件或公开指控让主角陷入误判。",
        "first3": "1异常事件，2证据指向错误对象，3出现第二解释。",
        "first10": "每2集翻一次证据方向，第10集揭出更大的旧案。",
        "midgame": "从个人疑案升级为组织、家庭或旧案系统。",
        "pitfalls": ["只藏信息", "没有情绪受害者", "线索不改变行动"],
    },
    "未分类待判断/其他": {
        "aliases": [],
        "emotion": "强情绪压迫和持续反转",
        "promise": "先确定可见压迫、关系债和反击工具，再归入明确赛道。",
        "opening": "用公开压迫或不可逆事件替代背景介绍。",
        "first3": "1压迫，2阻碍，3小反击或更大问题出现。",
        "first10": "每集一个行动事件，每3集一次关系或证据升级。",
        "midgame": "把个人冲突升级到资源、规则、身份或舆论系统。",
        "pitfalls": ["类型承诺不清", "爽点分散", "支线太多"],
    },
}


DIALOGUE_PATTERNS: list[dict[str, Any]] = [
    {
        "id": "d001",
        "function": "公开羞辱",
        "use_for": ["追妻火葬场", "霸总", "家庭伦理", "战神"],
        "pattern": "压迫者先给主角定罪，旁观者站队，主角只抓住一个可验证事实反问。",
        "avoid": "不要让主角长篇解释身世；第一场只留一个证据钩子。",
    },
    {
        "id": "d002",
        "function": "低位反击",
        "use_for": ["复仇", "赘婿", "战神", "神豪"],
        "pattern": "主角不解释全部底牌，只用当前规则反打一个小目标。",
        "avoid": "不要一次揭完身份；反击后必须引来更大压力。",
    },
    {
        "id": "d003",
        "function": "误判试探",
        "use_for": ["霸总", "虐恋", "追妻火葬场"],
        "pattern": "误判者用旧认知试探主角，主角用沉默或半句真相制造迟疑。",
        "avoid": "不要靠误会硬拖；每次试探都要产生行动后果。",
    },
    {
        "id": "d004",
        "function": "证据摊牌",
        "use_for": ["复仇", "悬疑", "家庭伦理"],
        "pattern": "先亮证据功能，再亮证据来源，最后留一个未公开的更大证据。",
        "avoid": "不要一口气解释全部前因后果。",
    },
    {
        "id": "d005",
        "function": "追悔求见",
        "use_for": ["追妻火葬场", "虐恋"],
        "pattern": "追悔者提出补偿，主角指出补偿无法覆盖的具体伤害。",
        "avoid": "不要只写哭和道歉；必须有行动成本。",
    },
    {
        "id": "d006",
        "function": "亲子线索",
        "use_for": ["萌宝", "家庭伦理"],
        "pattern": "孩子说出只有亲缘或旧案相关者才知道的信息，成年人误读。",
        "avoid": "孩子不能只卖萌，必须推动线索或关系选择。",
    },
    {
        "id": "d007",
        "function": "强者身份露一角",
        "use_for": ["战神", "神豪", "修仙"],
        "pattern": "旁人看不懂主角动作，只有更高层人物意识到身份异常。",
        "avoid": "不要让所有人立刻跪服。",
    },
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def norm(value: str) -> str:
    return re.sub(r"[\s\-_《》【】()（）,，.。!！:：;；、\"“”'’`|/]+", "", value).lower()


def tokens(query: str) -> list[str]:
    base = [x for x in re.split(r"[\s,，、/|]+", query.strip()) if x]
    lexicon = sorted({word for profile in TYPE_PROFILES.values() for word in profile["aliases"]})
    lexicon += ["第一屏", "前3集", "前10集", "中段", "钩子", "证据", "误会", "反击", "认亲", "身份", "羞辱", "追悔"]
    for word in lexicon:
        if word and word in query and word not in base:
            base.append(word)
    return base


def infer_profile(category: str, title: str = "") -> tuple[str, dict[str, Any]]:
    if category in TYPE_PROFILES:
        return category, TYPE_PROFILES[category]
    hay = f"{category} {title}"
    for name, profile in TYPE_PROFILES.items():
        if any(alias and alias in hay for alias in profile["aliases"]):
            return name, profile
    return "未分类待判断/其他", TYPE_PROFILES["未分类待判断/其他"]


def read_body(path: Path, max_chars: int | None = None) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "## 正文" in text:
        text = text.split("## 正文", 1)[1]
    text = text.strip()
    if max_chars:
        return text[:max_chars]
    return text


def extract_title_and_meta(path: Path, source_root: Path) -> dict[str, Any]:
    rel = path.relative_to(source_root)
    category = rel.parts[0].replace("_", "/") if len(rel.parts) > 1 else "未分类待判断/其他"
    title = path.stem
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines()[:20]:
        if line.startswith("# "):
            title = line[2:].strip() or title
            break
    chars = len(read_body(path))
    episode_match = re.search(r"(\d+)\s*[-－—]\s*(\d+)\s*集|[（(](\d+)\s*集[）)]", path.name)
    episode_count = None
    if episode_match:
        if episode_match.group(2):
            episode_count = int(episode_match.group(2))
        elif episode_match.group(3):
            episode_count = int(episode_match.group(3))
    return {
        "title": title,
        "category": category,
        "relative_path": str(rel),
        "chars": chars,
        "episode_count": episode_count,
        "is_full_length": bool(episode_count and episode_count >= 50) or chars >= 30000,
    }
