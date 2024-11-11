from .account import Account
from .investment import Investment

class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, account_name: str) -> Account:
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        net_worth = sum(account.balance for account in self.accounts)
        net_worth += sum(investment.calculate_value() for investment in self.investments)
        return net_worth
