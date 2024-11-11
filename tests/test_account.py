import unittest
from finances.account import Account
from finances.transaction import Transaction
from datetime import datetime

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Conta Corrente")

    def test_instance(self):
        self.assertIsInstance(self.account, Account)

    def test_add_transaction(self):
        transaction = self.account.add_transaction(100.0, 1, "Test Transaction")
        self.assertIsInstance(transaction, Transaction)
        self.assertIn(transaction, self.account.transactions)

    def test_get_transactions(self):
        self.account.add_transaction(100.0, 1, "Test Transaction 1")
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 1)

if __name__ == "__main__":
    unittest.main()
