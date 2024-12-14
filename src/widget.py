from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """
    Функция, которая принимает на вход тип карты или счёта и
    возвращает замаскированный счёт или замаскированный номер карты
    """
    if user_input == "":
        raise AssertionError ("Не введены данные")

    if user_input[-20:].isnumeric():
        return user_input[0:-20] + get_mask_account(user_input)
    else:
        return get_mask_card_number(user_input)


def get_date(user_date: str) -> str:
    """
    Функция, которая меняет формат даты
    """
    if user_date == "":
        raise AssertionError ("Не введена дата")

    if "-" in user_date[0:10]:
        return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[0:4]}"
    else:
        return f"{user_date[6:8]}.{user_date[4:6]}.{user_date[0:4]}"
