import unittest
from ledger import ExpenseService


class TestExpenseService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ExpenseService(monthly_budget=500.0)

    def test_add_and_total_expenses(self) -> None:
        self.service.add_expense("Cloud Hosting", "infra", 120.50)
        self.service.add_expense("Domain Renewal", "infra", 19.50)
        self.assertEqual(self.service.total_spent(), 140.00)
        self.assertEqual(self.service.remaining_budget(), 360.00)

    def test_filter_by_category(self) -> None:
        self.service.add_expense("Team Lunch", "food", 45.00)
        self.service.add_expense("CI Runner", "infra", 30.00)
        infra = self.service.list_expenses(category="INFRA")
        self.assertEqual(len(infra), 1)
        self.assertEqual(infra[0].title, "CI Runner")

    def test_rejects_non_positive_amount(self) -> None:
        with self.assertRaises(ValueError):
            self.service.add_expense("Invalid", "misc", 0)


if __name__ == "__main__":
    unittest.main()
