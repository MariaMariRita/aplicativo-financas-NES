from datetime import datetime
from .account import Account

class Investment:
    '''
    Classe para representar os investimentos
    Atributos:
    type (int): Identificador de um tipo de investimento armazenado em settings.py;
    initial_amount (float): Valor inicial do investimento;
    date_purchased (datetime): Data da compra do investimento;
    rate_of_return (float): Taxa mensal de retorno (somente aplicada a mês cheio);
    client (Client): Cliente dono do investimento;

    '''
    def __init__(self, type: int, initial_amount: float, rate_of_return: float) -> None:
        '''Inidicaliza um objeto Investiment'''
        self.type = type
        self.initial_amount = initial_amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return

    def calculate_value(self) -> float:
        '''Calcula o valor do investimento'''
        months_elapsed = (datetime.now().year - self.date_purchased.year) * 12 + (datetime.now().month - self.date_purchased.month)
        return self.initial_amount * ((1 + self.rate_of_return) ** months_elapsed)

    def sell(self, account: Account) -> None:
        '''Vende o investimento e deposita o valor em uma conta'''
        value = self.calculate_value()
        accoun
        t.add_transaction(value, category=999, description="Venda de Investimento")

    def generate_report(client: Client) -> str:
        '''Gera um relatório financeiro para um cliente com todas as suas transações e investimentos.'''

        report = f"Relatório Financeiro - Cliente: {client.name}\n"
        report += f"Email: {client.email}\n\n"
        report += "Investimentos:\n"
        for investment in client.investments:
            report += f"Tipo: {investment.investment_type}, Valor Inicial: {investment.initial_amount}, Valor Atual: {investment.calculate_value()}\n"
        report += "\nTransações:\n"
        for account in client.accounts:
            for transaction in account.transactions:
                report += f"Data: {transaction.date}, Categoria: {transaction.category}, Valor: {transaction.amount}, Descrição: {transaction.description}\n"
        return report


    def future_value_report(client: Client, date: datetime) -> str:
        """Gera um relatório de projeção de rendimentos futuros para os investimentos de um cliente até uma data específica."""
        report = f"Projeção de Rendimentos Futuros - Cliente: {client.name}\n"
        report += f"Data do Relatório: {date}\n\n"
        for investment in client.investments:
            months_to_project = (date - investment.date_purchased).days // 30
            future_value = investment.initial_amount * (1 + investment.rate_of_return) ** months_to_project
            report += f"Tipo: {investment.investment_type}, Valor Inicial: {investment.initial_amount}, Projeção de Valor em {date}: {future_value}\n"
        return report