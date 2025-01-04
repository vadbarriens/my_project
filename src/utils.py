import json

def fin_transaction(path: str) -> list:
    """Возвращает список словарей о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as transaction_file:
            try:
                transaction_list = json.load(transaction_file)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    if type(transaction_list) is not list:
        return []
    return transaction_list




if __name__ == '__main__':
    print(fin_transaction("../data/operations.json"))