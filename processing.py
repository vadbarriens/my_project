def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:
    """
    функция, которая принимает список словарей
    и возвращает новый список словарей с ключом state,
    соответствующий указанному значению
    """
    new_list_of_dictionaries = []
    for i in list_of_dictionaries:
        for key, value in i.items():
            if value == state:
                new_list_of_dictionaries.append(i)
    return new_list_of_dictionaries


def sort_by_date(list_operations: list, reverse: bool = True) -> list:
    """
    функция, которая принимает список словарей
    и возвращает отсортированный список словарей по дате
    """
    sorted_list = sorted(list_operations, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
