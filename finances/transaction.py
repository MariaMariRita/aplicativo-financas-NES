from datetime import datetime

CATEGORIES = {
    1: "Pagamento",
    2: "Depósito",
    3: "Transferência",
}

class Transaction:
    def __init__(self, amount: float, category: int, description: str = "") -> None:
        if category not in CATEGORIES.keys():
            raise ValueError("Categoria inválida.")

        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.description = description

    def update(
        self,
        amount: float | None = None,
        category: int | None = None,
        description: str | None = None,
        date: datetime | None = None,
    ) -> None:
        if amount is not None:
            self.amount = amount
        if category is not None:
            if category not in CATEGORIES.keys():
                raise ValueError("Categoria inválida.")
            self.category = category
        if description is not None:
            self.description = description
        if date is not None:
            self.date = date

    def __str__(self):
        return f"Transação: {self.description} R$ {self.amount:.2f} ({CATEGORIES[self.category]})"
