from typing import Any
from unittest.mock import patch

from src.transactions import read_transactions_csv, read_transactions_excel


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
