def filter_by_currency(transactions, currency):

    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)
