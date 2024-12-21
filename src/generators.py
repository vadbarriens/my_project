def filter_by_currency(transactions, currency):

    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions):
    descript_transact = (x.get("description") for x in transactions)
    for x in descript_transact:
        yield x
