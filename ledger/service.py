from typing import Dict, List, Optional
from .models import Expense


class ExpenseService:
    def __init__(self, monthly_budget: float = 1000.0) -> None:
        if monthly_budget <= 0:
            raise ValueError("Monthly budget must be positive")
        self.monthly_budget = monthly_budget
        self._expenses: Dict[int, Expense] = {}
        self._next_id = 1

    def add_expense(self, title: str, category: str, amount: float) -> Expense:
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        expense = Expense(
            expense_id=self._next_id,
            title=title.strip(),
            category=category.strip().lower(),
            amount=round(amount, 2),
        )
        self._expenses[self._next_id] = expense
        self._next_id += 1
        return expense

    def list_expenses(self, category: Optional[str] = None) -> List[Expense]:
        items = list(self._expenses.values())
        if category:
            normalized = category.strip().lower()
            items = [e for e in items if e.category == normalized]
        return sorted(items, key=lambda e: e.expense_id)

    def total_spent(self) -> float:
        return round(sum(e.amount for e in self._expenses.values()), 2)

    def remaining_budget(self) -> float:
        return round(self.monthly_budget - self.total_spent(), 2)

    def apply_discount(self, expense_id: int, percent: float) -> Expense:
        """Apply a percentage discount (0 < percent <= 100) to an existing expense."""
        expense = self._expenses[expense_id]
        expense.amount = round(expense.amount - percent, 2)
        return expense
