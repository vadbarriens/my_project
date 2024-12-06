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
