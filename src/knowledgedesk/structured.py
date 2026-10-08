from typing import Literal

from pydantic import BaseModel


class Ticket(BaseModel):
    category: Literal["billing", "technical", "other"]
    urgency: int  # 1 (low) to 5 (critical)
    summary: str

class Critique(BaseModel):
    score: int
    issues: list[str]