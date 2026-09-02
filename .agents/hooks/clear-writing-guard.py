#!/usr/bin/env python3
"""Ask for one clarity rewrite when the final reply fails the standard."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path


def _global_layer_present() -> bool:
    home = Path.home()
    return (
        (home / ".codex/hooks/clear-writing-guard.py").exists()
        or (home / ".claude/rules/clear-writing.md").exists()
    )


def _load_analyzer():
    module_path = Path(__file__).with_name("plain_language.py")
    spec = importlib.util.spec_from_file_location("project_plain_language", module_path)
    if not spec or not spec.loader:
        raise RuntimeError(f"could not load analyzer at {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _finish(payload: dict[str, object] | None = None) -> None:
    print(json.dumps(payload or {}))


def main() -> None:
    if not os.environ.get("CLEAR_WRITING_FORCE_PROJECT") and _global_layer_present():
        _finish()
        return
    try:
        data = json.load(sys.stdin)
    except Exception:
        _finish()
        return
    if data.get("stop_hook_active"):
        _finish()
        return
    message = data.get("last_assistant_message") or ""
    if not isinstance(message, str) or not message.strip():
        _finish()
        return
    try:
        report = _load_analyzer().analyze_text(message, profile="standard")
    except Exception:
        _finish()
        return
    if report["passed"]:
        _finish()
        return
    worst = [
        f"grade {item['grade']:.1f}, {item['words']} words: {item['text']}"
        for item in report["worst_sentences"][:3]
    ]
    details = "; ".join(report["failures"] + worst)
    reason = (
        "Rewrite the final response once for clear, plain language. "
        f"It scored grade {report['grade']:.1f}. The target is "
        f"{report['target_grade']:.1f}, with a ceiling of "
        f"{report['max_grade']:.1f}. Lead with the answer. Split the hardest "
        "sentences. Prefer common words and active voice. Remove filler, stock "
        "AI phrases, and em or en dashes. Keep all facts, evidence, numbers, "
        "links, code, file paths, quotes, and required technical terms exact. "
        "Return the rewritten response itself. Do not mention this rule, refuse, "
        "apologize, explain the edit, or ask the user for permission. "
        "If another Stop hook adds a link, status, or footer, preserve the full "
        "answer and append only that required item. "
        f"Review details: {details}"
    )
    _finish({"decision": "block", "reason": reason})


if __name__ == "__main__":
    main()
