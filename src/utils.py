import json
from typing import Any

from src.external_api import convert_transaction


def fin_transaction(path: str) -> list:
    """Возвращает список словарей о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as transaction_file:
            try:
                transaction_list = json.load(transaction_file)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    if type(transaction_list) is not list:
        return []
    return transaction_list


def transaction_amount(trans: dict) -> Any:
    """Выводит сумму по транзакции в рублях, если валюта иная, то конвертирует её"""
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        amount = trans["operationAmount"]["amount"]
    else:
        amount = convert_transaction(trans)
    return amount
