from finances.client import Client
from finances.account import Account
from finances.investment import Investment

def client() -> Client:
    """Cria uma instância do Client para uso nos testes."""
    return Client("Test Client")

def test_instance(client: Client) -> None:
    """Testa se a instância criada é do tipo Client."""
    assert isinstance(client, Client)

def test_add_account(client: Client) -> None:
    """Testa se a conta é adicionada corretamente ao cliente."""
    account = client.add_account("Conta Corrente")
    assert isinstance(account, Account)
    assert account in client.accounts

def test_add_investment(client: Client) -> None:
    """Testa se o investimento é adicionado corretamente ao cliente."""
    investment = Investment(type=1, amount=1000.0, rate_of_return=0.05)
    client.add_investment(investment)
    assert investment in client.investments

def test_get_net_worth(client: Client) -> None:
    """Testa se o patrimônio líquido do cliente está correto."""
    account = client.add_account("Conta Corrente")
    account.balance = 500.0
    investment = Investment(type=1, amount=1000.0, rate_of_return=0.05)
    client.add_investment(investment)
    assert client.get_net_worth() == 1500.0
