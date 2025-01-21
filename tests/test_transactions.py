from typing import Any
from unittest.mock import patch

from src.transactions import (count_transactions_by_categories, get_filter_transactions, read_transactions_csv,
                              read_transactions_excel)


@patch("csv.DictReader")
def test_read_transactions_csv(mock_csv: Any) -> None:
    expected = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    mock_csv.return_value = expected
    assert read_transactions_csv(r"C:\Users\burin87\PycharmProjects\my_project1\data\transactions.csv") == expected
    mock_csv.assert_called_once()


@patch("src.transactions.pd.read_excel")
def test_read_transactions_excel(mock_excel: Any) -> None:
    expected = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    mock_excel.return_value.to_dict.return_value = expected
    assert read_transactions_excel("../data/transactions_1.xlsx") == expected
    mock_excel.assert_called_once()


def test_get_filter_transactions() -> None:
    transactions = [
        {"description": "Открытие вклада", "amount": 5000, "status": "EXECUTED", "date": "2023-12-01"},
        {"description": "Перевод с карты на карту", "amount": 1000, "status": "CANCELED", "date": "2023-11-15"},
        {"description": "Оплата услуг", "amount": 2000, "status": "PENDING", "date": "2023-12-05"},
        {"description": "Покупка билетов", "amount": 1500, "status": "CANCELED", "date": "2023-10-20"},
    ]
    keyword = "карта"
    result = get_filter_transactions(transactions, keyword)
    assert len(result) == 0, f"Должно быть 1 совпадение, а найдено {len(result)}"


def test_count_transactions_by_categories() -> None:
    transactions = [
        {"description": "Открытие вклада", "amount": 5000, "status": "EXECUTED", "date": "2023-12-01"},
    ]
    categories = ["вклада"]
    result = count_transactions_by_categories(transactions, categories)
    print(f"Результат подсчета: {result}")
    assert result["вклада"] == 1, f"Ожидалось 1 транзакция в категории 'вклад', но найдено {result['вклад']}"
