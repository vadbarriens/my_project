import csv
import pandas as pd
import re

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


def get_filter_transactions(list_dict: list, search_bar: str) -> list:
    """Фильтрует список транзакций по строке поиска"""
    list_transactions = []
    pattern = rf"\b{search_bar}[а-я]*\b"
    for transact in list_dict:
        if re.search(pattern, transact.get("description", ""), re.IGNORECASE):
            list_transactions.append(transact)
    return list_transactions
