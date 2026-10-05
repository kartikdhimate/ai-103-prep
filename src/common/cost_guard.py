import json
import os
from datetime import date
from pathlib import Path

_STATE = Path("out") / "token_usage.json"


def _load() -> dict:
    if _STATE.exists():
        data = json.loads(_STATE.read_text())
        if data.get("day") == date.today().isoformat():
            return data
    return {"day": date.today().isoformat(), "tokens": 0}


def record_tokens(count: int) -> int:
    """Add tokens to today's total and stop the script when over budget."""
    budget = int(os.getenv("DAILY_TOKEN_BUDGET", "200000"))
    state = _load()
    state["tokens"] += count
    _STATE.parent.mkdir(exist_ok=True)
    _STATE.write_text(json.dumps(state))
    if state["tokens"] > budget:
        raise RuntimeError(f"Daily token budget exceeded: {state['tokens']} > {budget}")
    return state["tokens"]
