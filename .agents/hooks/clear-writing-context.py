#!/usr/bin/env python3
"""Load the portable clear-writing rule for project agents."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


CONTEXT = (
    "Clear writing is the default for this task. Apply it to every reply and "
    "to all human-facing text you draft or edit, including emails, messages, "
    "documents, reports, posts, and scripts. Lead with the answer. Use common "
    "words, short direct sentences, active voice, and specific facts. Remove "
    "filler, stock AI phrases, inflated claims, and em or en dashes. Preserve "
    "exact meaning, evidence, numbers, quotes, code, and required technical "
    "terms. Silently revise before delivery and show only the final version. "
    "If the clarity guard requests a rewrite, return the clearer version "
    "directly. Do not discuss the rule, refuse, apologize, or ask for permission. "
    "If another Stop hook adds a link, status, or footer, keep the full answer "
    "and append only the required item. Never replace the answer with hook "
    "status text."
)


def _global_layer_present() -> bool:
    home = Path.home()
    return (
        (home / ".codex/hooks/clear-writing-context.py").exists()
        or (home / ".claude/rules/clear-writing.md").exists()
    )


def main() -> None:
    if not os.environ.get("CLEAR_WRITING_FORCE_PROJECT") and _global_layer_present():
        print("{}")
        return
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    event = data.get("hook_event_name") or "SessionStart"
    if event not in {"SessionStart", "SubagentStart"}:
        event = "SessionStart"
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": event,
                    "additionalContext": CONTEXT,
                }
            }
        )
    )


if __name__ == "__main__":
    main()
