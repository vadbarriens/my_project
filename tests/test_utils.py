from typing import Any
from unittest.mock import patch

from src.utils import fin_transaction, transaction_amount


def test_fin_transaction_nofile() -> None:
    assert fin_transaction("nofile") == []


def test_fin_transaction(path: Any) -> None:
    assert fin_transaction(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_fin_transaction_empty_list(path_empty_list: Any) -> None:
    assert fin_transaction(path_empty_list) == []


def test_fin_transaction_mistake_json(path_mistake_json: Any) -> None:
    assert fin_transaction(path_mistake_json) == []


def test_transaction_amount(transaction: Any) -> Any:
    assert transaction_amount(transaction) == 31957.58


@patch("src.utils.convert_transaction")
def test_convert_transaction_non_rub(mock_convert_transaction: Any, transaction1: dict) -> Any:
    mock_convert_transaction.return_value = 1000.0
    assert transaction_amount(transaction1) == 1000.0
