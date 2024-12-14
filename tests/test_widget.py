import pytest

@pytest.fixture

def my_number_card():
    return "Visa Platinum 7000792289606361"

from src.widget import mask_account_card, get_date

def test_mask_account_card_Visa(my_number_card):
    assert mask_account_card(my_number_card) == "Visa Platinum 7000 79** **** 6361"


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


def test_mask_account_card_no_numbers():
    with pytest.raises(AssertionError):
        mask_account_card("")


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("user_date, expected",
                         [("2005-08-09T18:31:42+03", "09.08.2005"),
                          ("2005-08-09T18:31:42+03:30", "09.08.2005"),
                          ("20050809T183142-0330", "09.08.2005"),
                          ("20050809T183142", "09.08.2005")])
def test_get_date_edge_case(user_date, expected):
    assert get_date(user_date) == expected


def test_get_date_no_date():
    with pytest.raises(AssertionError):
        get_date("")
