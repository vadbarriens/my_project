import csv
import pandas as pd


def read_transactions_csv(path: str) -> list:
    """Читает файл CSV и выдает список словарей транзакций"""
    with open(path, "r", encoding="utf-8") as file:
        list_csv_transaction = csv.DictReader(file)
        return list(list_csv_transaction)


def read_transactions_excel(path: str) -> list:
    """Читает файл excel и выдает список словарей транзакций"""
    df = pd.read_excel(path)
    list_excel_transact = df.to_dict(orient='records')
    return list(list_excel_transact)
