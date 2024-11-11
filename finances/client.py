from .account import Account
from .investment import Investment

class Client:
    '''Classe representantiva do cliente
    Atributos:
    name(str): Nome do cliente
    accounts(list[Account]): Contas do cliente
    investments(list[Investment]): Investimentos do cliente'''
    def __init__(self, name: str) -> None:
        '''Inicializa um objeto Client'''
        self.name = name
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, account_name: str) -> Account:
        '''Cria uma conta para o cliente'''
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        '''Adiciona um investimento para o cliente'''
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        '''Calcula o valor de todas as contas e investimentos do cliente''' 
        net_worth = sum(account.balance for account in self.accounts)
        net_worth += sum(investment.calculate_value() for investment in self.investments)
        return net_worth
