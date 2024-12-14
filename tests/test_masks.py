import pytest

from src.masks import get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


@pytest.mark.parametrize("card_number, expected", [("3758493047586756473", "3758493 04** **** 6473"),
                                                   ("5748394857683", "5 74** **** 7683"),
                                                   ("3748576940", " ** **** 6940")])
def test_get_mask_card_number_edge_case(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_no_number():
    with pytest.raises(AssertionError):
        get_mask_card_number("")
