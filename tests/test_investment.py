from finances.investment import Investment
from finances.account import Account
from datetime import datetime


def investment() -> Investment:
    """Cria uma instância de Investment para os testes."""
    return Investment(type=1, amount=1000.0, rate_of_return=0.05)

def test_investment_instance(investment: Investment) -> None:
    """Testa se a instância criada é do tipo Investment."""
    assert isinstance(investment, Investment)

def test_calculate_value(investment: Investment) -> None:
    """Testa o cálculo do valor futuro do investimento.
    """
    assert investment.calculate_value() >= 1000.0

def test_sell(investment: Investment) -> None:
    """Testa a venda do investimento e o depósito do valor na conta.
    """
    account = Account("Poupança")
    initial_balance = account.balance
    investment.sell(account)
    assert account.balance == initial_balance + investment.calculate_value()

