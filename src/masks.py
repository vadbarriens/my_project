import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks_logs.log",
    filemode="w",
    encoding="utf-8",
)


logger = logging.getLogger()


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты и возвращает маску
    """
    logger.info("запуск программы")
    if card_number == "":
        logger.error("не введен номер карты")
        raise AssertionError("Не введён номер карты")

    return f"{card_number[0:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Принимает номер счёта и возвращает маску
    """
    logger.info("маскировка номера счёта")
    return f"**{account_number[-4:]}"
