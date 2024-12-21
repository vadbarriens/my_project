def filter_by_currency(transactions: list, currency: str) -> iter:
    """Функция, которая принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if transactions == []:
        return iter([])
    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list) -> str:
    """Генератор, который принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди."""

    descript_transact = (x.get("description") for x in transactions)
    for x in descript_transact:
        yield x


def card_number_generator(start: int, stop: int) -> str:
    """Генератор, который выдает номера банковских карт в заданном диапазоне"""

    for x in range(start, stop + 1):
        necessity_zero = 16 - len(str(x))
        result = "0" * necessity_zero + str(x)
        result_number_card = f'{str(result)[:4]} {str(result)[4:8]} {str(result)[-8:-4]} {str(result)[-4:]}'

        yield result_number_card

