import csv
import pandas as pd


def read_transactions_csv(path: str) -> list:
    """Читает файл CSV и выдает список словарей транзакций"""
    with open(path, encoding='utf8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)


def read_transactions_excel(path: str) -> list:
    """Читает файл excel и выдает список словарей транзакций"""
    df = pd.read_excel(path)
    list_excel_transact = df.to_dict(orient='records')
    return list(list_excel_transact)
