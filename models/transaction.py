from datetime import date


class Transaction:
    def __init__(
            self,
            amount: float,
            transaction_type: str,
            category: str,
            description: str,
            transaction_date: date
    ):
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.description = description
        self.transaction_date = transaction_date

    def __str__(self):
        sign = "+" if self.transaction_date == "income" else "-"

        return (
            f"{self.transaction_date} | "
            f"{self.category:<15} | "
            f"{self.description:<25} | "
            f"{sign}${self.amount:.2f} "
        )