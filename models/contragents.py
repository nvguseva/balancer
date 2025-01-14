import uuid

class Contragent:
    def __init__(self, name: str, balance: float = 0.0):
        self.id = uuid.uuid4()
        self.name = name
        self.balance = balance

    def update_balance(self, amount: float):
        self.balance += amount

    def __repr__(self):
        return f"Contragent({self.name}, balance={self.balance})"