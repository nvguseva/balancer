from models.contragents import Contragent

class ContragentService:
    def __init__(self):
        self.contragents = []

    def add_contragent(self, name: str):
        contragent = Contragent(name)
        self.contragents.append(contragent)
        return contragent

    def get_contragent_by_name(self, name: str):
        return next((c for c in self.contragents if c.name == name), None)