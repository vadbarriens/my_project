def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты и возвращает маску
    """
    return f"{card_number[0:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Принимает номер счёта и возвращает маску
    """
    return f"**{account_number[-4:]}"
