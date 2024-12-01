from src.masks import get_mask_account, get_mask_card_number

card_number = str(input("введите номер карты: "))
print(get_mask_card_number(card_number))

account_number = str(input("введите номер счёта: "))
print(get_mask_account(account_number))
