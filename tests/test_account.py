from finances.account import Account
from finances.transaction import Transaction


def account() -> Account:
    """Cria uma instância de Account para ser utilizada nos testes."""
    return Account("Conta Corrente")

def test_instance(account: Account) -> None:
    """Teste para verificar se a instância criada é do tipo Account."""
    assert isinstance(account, Account)

def test_add_transaction(account: Account) -> None:
    """
    Teste para verificar a adição de uma transação à conta.
    """
    transaction = account.add_transaction(100.0, 1, "Test Transaction")
    assert isinstance(transaction, Transaction)
    assert transaction in account.transactions

def test_get_transactions(account: Account) -> None:
    """
    Teste para verificar a recuperação de transações da conta.
    """
    account.add_transaction(100.0, 1, "Test Transaction 1")
    transactions: List[Transaction] = account.get_transactions()
    assert len(transactions) == 1
