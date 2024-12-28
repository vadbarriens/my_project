import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(my_number: str) -> None:
    assert get_mask_card_number(my_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("3758493047586756473", "3758493 04** **** 6473"),
        ("5748394857683", "5 74** **** 7683"),
        ("3748576940", " ** **** 6940"),
    ],
)
def test_get_mask_card_number_edge_case(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_no_number() -> None:
    with pytest.raises(AssertionError):
        get_mask_card_number("")


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("123423094325094055678909876543", "**6543"),
        ("123 346 899 0 797 6374857", "**4857"),
        ("649.30.485.7.4635.2176453", "**6453"),
    ],
)
def test_get_mask_account_edge_case(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_short_number() -> None:
    assert get_mask_account("135872879") == "**2879"
