import pandas as pd
import csv


def read_transactions_csv(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        list_csv_transaction = csv.DictReader(file)
        return list(list_csv_transaction)


def read_transactions_excel(path: str) -> list:
    df = pd.read_excel(path)
    list_excel_transact = df.to_dict(orient='records')
    return list(list_excel_transact)
