import json
import logging
from typing import Any

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(r"C:\Users\burin87\PycharmProjects\my_project1\logs\utils_logs.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


from src.external_api import convert_transaction


def fin_transaction(path: str) -> list:
    """Возвращает список словарей о финансовых транзакциях"""
    logger.info("запуск программы")
    try:
        with open(path, "r", encoding="utf-8") as transaction_file:
            try:
                logger.info("загрузка транзакций")
                transaction_list = json.load(transaction_file)
            except json.JSONDecodeError:
                logger.error("ошибка декодирования файла")
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Файл не найден")
        return []
    if type(transaction_list) is not list:
        logger.info("список не содержит транзакций")
        return []
    return transaction_list


def transaction_amount(trans: dict) -> Any:
    """Выводит сумму по транзакции в рублях, если валюта иная, то конвертирует её"""
    logger.info("запуск программы")
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("сумма не конвертировалась")
        amount = float(trans["operationAmount"]["amount"])
    else:
        logger.info("сумма конвертировалась")
        amount = convert_transaction(trans)
    return amount
