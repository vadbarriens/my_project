import pytest
from typing import Any
from src.decorators import log


def test_log(capsys: Any) -> Any:
    @log(filename=None)
    def my_function() -> Any:
        captured = capsys.readouterr()
        assert captured.out == "my_function ok\n"


def test_log_console() -> Any:
    @log(filename=None)
    def my_function() -> Any:
        assert my_function(3, 2) == "my_function ok"


def test_log_success() -> Any:
    @log(filename="mylog.txt")
    def my_function() -> Any:
        assert my_function() == ""


def test_log_exception() -> Any:
    @log(filename=None)
    def my_function() -> Any:
        with pytest.raises(TypeError) as exc_info:
            my_function("3", 2)

def test_log_exception1() -> Any:
    @log(filename=None)
    def my_function() -> Any:
        with pytest.raises(TypeError) as exc_info:
            my_function("3", 2)
