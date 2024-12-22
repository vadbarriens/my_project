import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list, currency: str) -> iter:
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_no_currency(transactions: list, currency_1: str) -> iter:
    generator = filter_by_currency(transactions, currency_1)
    assert not list(generator)


def test_filter_by_currency_no_list(transactions_1: list, currency: str) -> iter:
    generator = filter_by_currency(transactions_1, currency)
    assert not list(generator)


def test_transaction_descriptions(transactions: list) -> str:
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"


"Перевод со счета на счет"
"Перевод со счета на счет"
"Перевод с карты на карту"
"Перевод организации"


def test_transaction_descriptions_not_list(transactions_1: list) -> str:
    generator = transaction_descriptions(transactions_1)
    assert not list(generator)


def test_card_number_generator(start: int, stop: int) -> str:
    generator = card_number_generator(start, stop)
    assert next(generator) == "0000 0000 0000 0598"


"0000 0000 0000 0599"
"0000 0000 0000 0600"
"0000 0000 0000 0601"


def test_card_number_generator_stop(start_1: int, stop_1: int) -> str:
    generator = card_number_generator(start_1, stop_1)
    assert next(generator) == "9999 9999 9999 9997"


"9999 9999 9999 9998"
"9999 9999 9999 9999"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (5, 6, ["0000 0000 0000 0005", "0000 0000 0000 0006"]),
        (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_param(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert list(generator) == expected
