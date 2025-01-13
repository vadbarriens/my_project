import logging


logger = logging.getLogger('masks')
file_handler = logging.FileHandler('../logs/masks_logs.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug('сообщение уровня debug')
logger.info('сообщение уровня info')
logger.warning('сообщение уровня warning')
logger.error('сообщение уровня error')
logger.critical('сообщение уровня critical')


def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты и возвращает маску
    """
    if card_number == "":
        raise AssertionError("Не введён номер карты")

    return f"{card_number[0:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Принимает номер счёта и возвращает маску
    """
    return f"**{account_number[-4:]}"
