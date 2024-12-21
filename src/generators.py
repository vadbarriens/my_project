import random


def filter_by_currency(transactions, currency):

    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions):
    descript_transact = (x.get("description") for x in transactions)
    for x in descript_transact:
        yield x


def card_number_generator(start, stop):
        for x in range(start, stop + 1):
            necessity_zero = 16 - len(str(x))
            result = "0" * necessity_zero + str(x)
            result_number_card = f'{str(result)[:4]} {str(result)[4:8]} {str(result)[-8:-4]} {str(result)[-4:]}'

            yield result_number_card
