import pytest
@pytest.fixture
def my_list():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},]

from src.processing import filter_by_state

def test_filter_by_state(my_list):
    assert filter_by_state(my_list) == [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


# def test_filter_by_state_no_state():
#     assert filter_by_state([
#     {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
# ]) == []
#
#
# @pytest.mark.parametrize("list_of_dictionaries, expected", [
#         ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#           {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#           {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
#          [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#           {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]),
#         ([{"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
#           {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
#           {"id": 594226727, "date": "2018-09-12T21:27:25.241689"}], [])])
#
# def test_filter_by_state_edge_case(list_of_dictionaries, expected):
#     assert filter_by_state(list_of_dictionaries) == expected
