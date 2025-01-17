import pandas as pd
import csv


def read_transactions_csv(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        list_csv_transaction = csv.DictReader(file)
        return list(list_csv_transaction)
