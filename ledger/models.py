from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Expense:
    expense_id: int
    title: str
    category: str
    amount: float
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
