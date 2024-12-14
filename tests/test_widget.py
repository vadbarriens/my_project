import pytest

from src.widget import mask_account_card

def test_mask_account_card_Visa():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_Master_card():
    assert mask_account_card("Maestro 7000792289606361") == "Maestro 7000 79** **** 6361"


def test_mask_account_card_account_number():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


@pytest.mark.parametrize("account_card_number, expected",
                         [("Visa Platinum 7000324564575687", "Visa Platinum 7000 32** **** 5687"),
                          ("Visa 3849586758493049", "Visa 3849 58** **** 3049"),
                          ("Maestro 8574637485768594", "Maestro 8574 63** **** 8594"),
                          ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card_edge_case(account_card_number, expected):
    assert mask_account_card(account_card_number) == expected


def test_mask_account_card():
    with pytest.raises(AssertionError):
        mask_account_card("")


