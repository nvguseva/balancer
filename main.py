from services.contragent_service import ContragentService
from services.cash_flow_service import CashFlowService


if __name__ == "__main__":
    contragent_service = ContragentService()
    cash_flow_service = CashFlowService()

    # Добавляем контрагента
    contragent = contragent_service.add_contragent("Иван Иванов")
    print(contragent)

    # Добавляем доход
    income = cash_flow_service.add_cash_flow("Зарплата", 50000, contragent, "income")
    print(income)

    # Добавляем расход
    expense = cash_flow_service.add_cash_flow("Покупка", 10000, contragent, "expense")
    print(expense)

    # Печатаем баланс контрагента
    print(f"Текущий баланс контрагента: {contragent.balance}")