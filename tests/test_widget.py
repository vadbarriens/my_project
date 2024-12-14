
from src.widget import mask_account_card

def test_mask_account_card_Visa():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_Master_card():
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 7000 79** **** 6361"


def test_mask_account_card_account_number():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"