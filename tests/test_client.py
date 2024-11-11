import unittest
from finances.client import Client
from finances.account import Account
from finances.investment import Investment

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("Test Client")

    def test_instance(self):
        self.assertIsInstance(self.client, Client)

    def test_add_account(self):
        account = self.client.add_account("Conta Corrente")
        self.assertIsInstance(account, Account)
        self.assertIn(account, self.client.accounts)

    def test_add_investment(self):
        investment = Investment(type=1, amount=1000.0, rate_of_return=0.05)
        self.client.add_investment(investment)
        self.assertIn(investment, self.client.investments)

    def test_get_net_worth(self):
        account = self.client.add_account("Conta Corrente")
        account.balance = 500.0
        investment = Investment(type=1, amount=1000.0, rate_of_return=0.05)
        self.client.add_investment(investment)
        self.assertEqual(self.client.get_net_worth(), 1500.0)

if __name__ == "__main__":
    unittest.main()
