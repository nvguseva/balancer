from datetime import datetime
from typing import Optional
from models.contragents import Contragent

class CashFlow:
    def __init__(self, name: str, amount: float, contragent: Contragent, type_: str, date: Optional[datetime] = None):
        self.name = name
        self.amount = amount
        self.contragent = contragent
        self.type_ = type_  # "income" или "expense"
        self.date = date or datetime.now()

    def __repr__(self):
        return f"CashFlow({self.name}, {self.amount}, type={self.type_}, date={self.date})"