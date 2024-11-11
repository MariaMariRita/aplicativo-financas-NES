from datetime import datetime
from .transaction import Transaction

class Account:
    '''
    Classe para representar contas e armazenar transações
    Atributos:
    name(str) -> Nome da conta
    balance(float) -> Saldo da conta
    transactions(list[Transaction]) -> Lista de transações na conta
    '''
    def __init__(self, name: str) -> None:
        '''inicializa um objeto conta'''
        self.name = name
        self.balance = 0.0
        self.transactions: List[Transaction] = []

    def add_transaction(self, amount: float, category: int, description: str = "") -> Transaction:
        '''Cria uma transação na conta'''
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.balance += amount
        return transaction

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, category: int = None) -> List[Transaction]:
        '''Gera uma lista de transações'''
        filtered_transactions = self.transactions #filtro de transações
        filtered_transactions = []
        #Filtragem por start_date
        if start_date:
            for t in filtered_transactions:
                if t.date >= start_date:
                    filtered_transactions.append(t)

        # Filtragem por end_date
        if end_date:
            for t in filtered_transactions:
                if t.date <= end_date:
                    filtered_transactions.append(t)

        # Filtragem por category
        if category is not None:
            for t in filtered_transactions:
                if t.category == category:
                    filtered_transactions.append(t)

        return filtered_transactions

