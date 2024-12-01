from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

card_number = str(input("введите номер карты: "))
print(get_mask_card_number(card_number))

account_number = str(input("введите номер счёта: "))
print(get_mask_account(account_number))

user_input = str(input("введите номер карты или счета: "))
print(mask_account_card(user_input))
