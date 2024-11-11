import unittest
from finances.investment import Investment
from finances.account import Account
from datetime import datetime

class TestInvestment(unittest.TestCase):
    def setUp(self):
        self.investment = Investment(type=1, amount=1000.0, rate_of_return=0.05)

    def test_instance(self):
        self.assertIsInstance(self.investment, Investment)

    def test_calculate_value(self):
        # Simula uma projeção de cálculo de valor futuro
        self.assertGreaterEqual(self.investment.calculate_value(), 1000.0)

    def test_sell(self):
        account = Account("Poupança")
        initial_balance = account.balance
        self.investment.sell(account)
        self.assertEqual(account.balance, initial_balance + self.investment.calculate_value())

if __name__ == "__main__":
    unittest.main()
