from datetime import datetime
from .account import Account

class Investment:
    def __init__(self, type: int, initial_amount: float, rate_of_return: float) -> None:
        self.type = type
        self.initial_amount = initial_amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return

    def calculate_value(self) -> float:
        months_elapsed = (datetime.now().year - self.date_purchased.year) * 12 + (datetime.now().month - self.date_purchased.month)
        return self.initial_amount * ((1 + self.rate_of_return) ** months_elapsed)

    def sell(self, account: Account) -> None:
        value = self.calculate_value()
        account.add_transaction(value, category=999, description="Venda de Investimento")
