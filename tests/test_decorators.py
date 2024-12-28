import pytest
from typing import Any
from src.decorators import log, my_function


def test_log(capsys: Any) -> Any:
    @log(filename=None)
    def my_function() -> Any:
        captured = capsys.readouterr()
        assert captured.out == "my_function ok\n"


def test_log_success() -> Any:
    @log(filename=None)
    def my_function() -> Any:
        assert my_function() == "my_function ok"


def test_log_console() -> Any:
    @log(filename="mylog.txt")
    def my_function() -> Any:
        assert my_function() == ""


def test_log_exception() -> Any:
    @log(filename=None)
    def my_function() -> Any:
        my_function("3", 2)
        assert my_function() == TypeError
