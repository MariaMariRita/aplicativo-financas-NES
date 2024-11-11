from finances import Transaction
from finances.transaction import CATEGORIES
from datetime import datetime

DEFAULT_AMOUNT = 100.0
DEFAULT_CATEGORY = 1
DEFAULT_DESCRIPTION = "Transação de teste"

def get_transaction():
    """Cria objeto Transaction com valores padrão"""
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

def test_transaction_instance():
    """Testa instanciação de transações"""
    tr = get_transaction()
    assert isinstance(tr, Transaction), "Falha ao instanciar um objeto Transaction"

def test_transaction_cat():
    """Testa se as categorias são validas"""
    tr = get_transaction()
    assert tr.category in CATEGORIES.keys(), "Categoria invalida"

def test_transaction_atributes():
    """Testa os tipos e valores dos atributos"""
    tr = get_transaction()
    # Checa os tipos
    assert type(tr.amount) is float, "Tipo incorreto para o valor."
    assert type(tr.date) is datetime, "Tipo incorreto para a data."
    assert type(tr.category) is int, "Tipo incorreto para a categoria."
    assert type(tr.description) is str, "Tipo incorreto para a descrição."
    # Checa os valores
    assert tr.amount == DEFAULT_AMOUNT, "Valore incorreto."
    assert tr.category == DEFAULT_CATEGORY, "Categoria incorreta."
    assert tr.description == DEFAULT_DESCRIPTION, "Descrição incorreta"

def test_transaction_update():
    """Checa se o comando update atualiza os atributos."""
    tr = get_transaction()
    tr.update(amount=200.0)
    assert tr.amount == 200.0, "Falha ao atualizar o valor."
    new_date = datetime.now()
    tr.update(date=new_date)
    assert tr.date == new_date, "Falha ao atualizar a data."
    tr.update(category=2)
    assert tr.category == 2, "Falha ao atualizar a categoria."
    tr.update(description="Teste")
    assert tr.description == "Teste", "Falha ao atualizar a descrição."

def test_transaction_representation():
    tr = get_transaction()
    expected = f"Transação: {DEFAULT_DESCRIPTION} R$ {DEFAULT_AMOUNT:.2f} ({CATEGORIES[DEFAULT_CATEGORY]})"
    assert str(tr) == expected, "Representação fora do formato esperado."
