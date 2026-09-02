#!/usr/bin/env python3
"""Check human-facing writing for clarity with a transparent ARI score.

This checker follows Hemingway's published editing ideas. It uses the
Automated Readability Index, so it does not claim score parity with Hemingway.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


PROFILES = {
    "accessible": {"target_grade": 6.0, "max_grade": 7.5},
    "sales": {"target_grade": 8.0, "max_grade": 9.5},
    "standard": {"target_grade": 9.0, "max_grade": 10.5},
    "technical": {"target_grade": 12.0, "max_grade": 14.0},
}

QUALIFIERS = (
    "a bit", "a little", "arguably", "basically", "fairly", "generally",
    "i believe", "i feel", "i guess", "i think", "kind of", "largely",
    "maybe", "perhaps", "possibly", "probably", "quite", "rather",
    "relatively", "seemingly", "somewhat", "sort of", "virtually",
)

SIMPLE_ALTERNATIVES = {
    "accordingly": "so",
    "additional": "more",
    "approximately": "about",
    "commence": "start",
    "demonstrate": "show",
    "endeavor": "try",
    "facilitate": "help",
    "implement": "use or set up",
    "in order to": "to",
    "indicate": "show",
    "leverage": "use",
    "numerous": "many",
    "obtain": "get",
    "prior to": "before",
    "subsequent": "next or later",
    "terminate": "end",
    "utilize": "use",
}

AI_ISMS = (
    "align with", "at its core", "crucial", "cutting-edge", "delve",
    "elevate", "enduring", "enhance", "foster", "furthermore",
    "game-changer", "groundbreaking", "here's the thing", "highlighting",
    "i hope this", "in conclusion", "in today's world", "intricate",
    "it is worth noting", "let's dive in", "moreover", "navigate the",
    "pivotal", "robust", "seamless", "showcase", "tapestry",
    "testament to", "underscore", "unlock the", "vibrant",
)

ADVERB_EXCEPTIONS = {
    "ally", "apply", "belly", "daily", "early", "family", "friendly",
    "holy", "jelly", "likely", "lively", "lonely", "lovely", "only",
    "reply", "silly", "supply", "ugly", "weekly", "woolly", "yearly",
}

WORD_RE = re.compile(r"[A-Za-z]+(?:['-][A-Za-z]+)*|\d+(?:[.,]\d+)*")
PASSIVE_RE = re.compile(
    r"\b(?:am|are|is|was|were|be|been|being|gets?|got)\s+"
    r"(?:\w+\s+){0,2}?(?:\w+(?:ed|en)|built|done|found|given|held|kept|known|"
    r"made|paid|put|read|run|said|seen|sent|set|shown|sold|taught|told|written)\b",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
MEMORY_CITATION_RE = re.compile(
    r"<oai-mem-citation>.*?</oai-mem-citation>", re.DOTALL | re.IGNORECASE
)
DIRECTIVE_RE = re.compile(r"(?m)^::[a-z-]+\{.*?\}\s*$")
HTML_RE = re.compile(r"<[^>]+>")


def clean_prose(text: str) -> str:
    """Remove code and markup that should not affect a prose score."""
    value = MEMORY_CITATION_RE.sub(" ", text or "")
    value = CODE_FENCE_RE.sub(" ", value)
    value = DIRECTIVE_RE.sub(" ", value)
    value = re.sub(r"`[^`]+`", " code ", value)
    value = re.sub(r"!\[([^]]*)\]\([^)]+\)", r" \1 ", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r" \1 ", value)
    value = re.sub(r"<(https?://[^|>]+)\|([^>]+)>", r" \2 ", value)
    value = URL_RE.sub(" link ", value)
    value = HTML_RE.sub(" ", value)
    value = re.sub(
        r"(?m)^\s{0,3}(?:#{1,6}\s+|>\s*|[-+*]\s+|\d+[.)]\s+)",
        "",
        value,
    )
    value = re.sub(r"(?m)(?:^|\s)#[A-Za-z0-9_]+", " ", value)
    value = re.sub(r"(?m)^\s*\d{1,2}:\d{2}(?::\d{2})?\s+", "", value)
    value = value.replace("|", " ")
    return re.sub(r"[ \t]+", " ", value).strip()


def split_sentences(text: str) -> list[str]:
    """Split prose while treating list items and paragraph lines as sentences."""
    cleaned = clean_prose(text)
    if not cleaned:
        return []
    sentences: list[str] = []
    for line in cleaned.splitlines():
        line = line.strip()
        if not line:
            continue
        for part in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])", line):
            part = part.strip()
            if WORD_RE.search(part):
                sentences.append(part)
    return sentences


def _words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def ari_grade(text: str) -> float:
    sentences = split_sentences(text)
    words = _words(" ".join(sentences))
    if not words:
        return 0.0
    characters = sum(len(re.sub(r"[^A-Za-z0-9]", "", word)) for word in words)
    score = (
        4.71 * (characters / len(words))
        + 0.5 * (len(words) / max(len(sentences), 1))
        - 21.43
    )
    return round(max(0.0, score), 1)


def _phrase_hits(text: str, phrases: tuple[str, ...] | dict[str, str]) -> list[str]:
    lowered = text.lower()
    candidates = phrases.keys() if isinstance(phrases, dict) else phrases
    return [
        phrase
        for phrase in candidates
        if re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", lowered)
    ]


def _adverbs(words: list[str]) -> list[str]:
    hits = []
    for raw in words:
        word = raw.lower().strip("'-")
        if len(word) > 4 and word.endswith("ly") and word not in ADVERB_EXCEPTIONS:
            hits.append(word)
    return hits


def _sentence_report(sentence: str, target_grade: float) -> dict[str, object]:
    words = _words(sentence)
    grade = ari_grade(sentence)
    severity = "clear"
    if len(words) >= 35 or (len(words) >= 12 and grade > target_grade + 4):
        severity = "red"
    elif len(words) >= 25 or (len(words) >= 10 and grade > target_grade + 2):
        severity = "yellow"
    return {
        "text": sentence[:240],
        "words": len(words),
        "grade": grade,
        "severity": severity,
    }


def analyze_text(text: str, *, profile: str = "standard") -> dict[str, object]:
    if profile not in PROFILES:
        raise ValueError(f"unknown profile: {profile}")
    target = float(PROFILES[profile]["target_grade"])
    ceiling = float(PROFILES[profile]["max_grade"])

    prose = clean_prose(text)
    sentences = split_sentences(text)
    words = _words(" ".join(sentences))
    sentence_reports = [_sentence_report(sentence, target) for sentence in sentences]
    counts = Counter(report["severity"] for report in sentence_reports)
    red_sentences = [item for item in sentence_reports if item["severity"] == "red"]
    grade = ari_grade(text)

    failures = []
    em_dashes = text.count("\N{EM DASH}")
    en_dashes = text.count("\N{EN DASH}")
    if em_dashes:
        failures.append(f"contains {em_dashes} em dash(es)")
    if en_dashes:
        failures.append(f"contains {en_dashes} en dash(es)")
    if len(words) >= 30 and grade > ceiling:
        failures.append(f"grade {grade:.1f} exceeds the {profile} ceiling of {ceiling:.1f}")
    if (
        len(sentences) >= 6
        and len(red_sentences) >= 3
        and len(red_sentences) / len(sentences) > 0.25
    ):
        failures.append(
            f"{len(red_sentences)} of {len(sentences)} sentences are far above the target"
        )

    passive_hits = PASSIVE_RE.findall(prose)
    adverb_hits = _adverbs(words)
    qualifier_hits = _phrase_hits(prose, QUALIFIERS)
    simpler_hits = _phrase_hits(prose, SIMPLE_ALTERNATIVES)
    ai_ism_hits = _phrase_hits(prose, AI_ISMS)

    warnings = []
    if counts["yellow"]:
        warnings.append(f"{counts['yellow']} hard-to-read sentence(s)")
    if counts["red"]:
        warnings.append(f"{counts['red']} very-hard-to-read sentence(s)")
    if passive_hits:
        warnings.append(f"{len(passive_hits)} possible passive-voice phrase(s)")
    if adverb_hits:
        warnings.append(f"{len(adverb_hits)} possible adverb(s)")
    if qualifier_hits:
        warnings.append(f"{len(qualifier_hits)} qualifier type(s)")
    if simpler_hits:
        warnings.append(f"{len(simpler_hits)} phrase type(s) with simpler alternatives")
    if ai_ism_hits:
        warnings.append(f"{len(ai_ism_hits)} AI-tell phrase type(s)")

    paragraphs = len(
        [part for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]
    ) if text.strip() else 0
    return {
        "passed": not failures,
        "profile": profile,
        "target_grade": target,
        "max_grade": ceiling,
        "grade": grade,
        "stats": {
            "words": len(words),
            "sentences": len(sentences),
            "paragraphs": paragraphs,
            "reading_seconds": round(len(words) / 200 * 60) if words else 0,
        },
        "sentence_counts": {
            "clear": counts["clear"],
            "yellow": counts["yellow"],
            "red": counts["red"],
        },
        "failures": failures,
        "warnings": warnings,
        "signals": {
            "adverbs": sorted(set(adverb_hits)),
            "ai_isms": ai_ism_hits,
            "passive_voice_count": len(passive_hits),
            "qualifiers": qualifier_hits,
            "simpler_alternatives": {
                phrase: SIMPLE_ALTERNATIVES[phrase] for phrase in simpler_hits
            },
        },
        "worst_sentences": sorted(
            [item for item in sentence_reports if item["severity"] != "clear"],
            key=lambda item: (
                item["severity"] == "red",
                item["grade"],
                item["words"],
            ),
            reverse=True,
        )[:5],
    }


def format_report(report: dict[str, object]) -> str:
    status = "PASS" if report["passed"] else "FAIL"
    stats = report["stats"]
    lines = [
        f"{status}: {report['profile']} plain-language check",
        (
            f"Grade {report['grade']:.1f} "
            f"(target {report['target_grade']:.1f}, ceiling {report['max_grade']:.1f})"
        ),
        (
            f"{stats['words']} words, {stats['sentences']} sentences, "
            f"{stats['paragraphs']} paragraphs, about {stats['reading_seconds']} seconds"
        ),
    ]
    for failure in report["failures"]:
        lines.append(f"FAIL: {failure}")
    for warning in report["warnings"]:
        lines.append(f"WARN: {warning}")
    for item in report["worst_sentences"][:3]:
        lines.append(
            f"{str(item['severity']).upper()} grade {item['grade']:.1f}, "
            f"{item['words']} words: {item['text']}"
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="File to check. Reads stdin when omitted.")
    parser.add_argument("--profile", choices=sorted(PROFILES), default="standard")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()

    text = Path(args.path).read_text() if args.path else sys.stdin.read()
    report = analyze_text(text, profile=args.profile)
    print(json.dumps(report, indent=2) if args.json else format_report(report))
    if not report["passed"] and not args.report_only:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
