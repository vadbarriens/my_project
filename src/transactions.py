import csv
import re

import pandas as pd


def read_transactions_csv(path: str) -> list:
    """Читает файл CSV и выдает список словарей транзакций"""
    with open(path, encoding="utf8") as f:
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)


def read_transactions_excel(path: str) -> list:
    """Читает файл excel и выдает список словарей транзакций"""
    df = pd.read_excel(path)
    list_excel_transact = df.to_dict(orient="records")
    return list(list_excel_transact)


def get_filter_transactions(transactions: list, search_bar: str) -> list:
    """Фильтрует список транзакций по строке поиска"""
    list_transactions = []
    pattern = rf"\b{search_bar}[а-я]*\b"
    for transact in transactions:
        if re.search(pattern, transact.get("description", ""), re.IGNORECASE):
            list_transactions.append(transact)
    return list_transactions


def count_transactions_by_categories(transactions: list, categories: list) -> dict:
    """Считает количество банковских операций по категориям"""
    result = {}
    for category in categories:
        result[category] = 0  # Инициализируем счётчик для каждой категории

    for transact in transactions:
        description = transact.get("description", "")
        for category in categories:
            if re.search(rf"\b{category}[а-я]*\b", description, re.IGNORECASE):
                result[category] += 1
    return result
