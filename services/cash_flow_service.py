from models.contragents import Contragent
from models.cash_flows import CashFlow

class CashFlowService:
    def __init__(self):
        self.cash_flows = []

    def add_cash_flow(self, name: str, amount: float, contragent: Contragent, type_: str):
        cash_flow = CashFlow(name, amount, contragent, type_)
        self.cash_flows.append(cash_flow)
        contragent.update_balance(amount if type_ == "income" else -amount)
        return cash_flow