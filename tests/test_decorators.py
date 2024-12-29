import os
import pytest
from typing import Any
from config import path
from src.decorators import log


def test_log(capsys: Any) -> Any:
    @log(filename=None)
    def my_function1(x: int, y: int) -> int:
        return x + y

    my_function1(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "my_function1 ok\n"


def test_log_successful() -> Any:
    @log(filename="mylog.txt")
    def my_func(x: int, y: int) -> int:
        return x * y
        assert my_func(x, y) == ""

    my_func(2, 3)


def test_log_except() -> Any:
    @log(filename=None)
    def my_func1(x: int, y: int) -> int:
        return x * y
        with pytest.raises(ValueError, match="my_function error: ValueError. Inputs: (2, '3'), {}"):
            my_func1(2)


def test_log_err() -> Any:
    @log(filename="mylog.txt")
    def func2(a: float, b: float) -> float:
        return a / b

    func2(2, 0)
    with open(os.path.join(path, "mylog.txt"), "r", encoding="utf-8") as f:
        err = f.read().split("\n")
    assert err[-2] == "func2 error: ZeroDivisionError. Inputs: (2, 0), {}"


def test_log_err1() -> Any:
    @log(filename="mylog.txt")
    def func3(a: float, b: float) -> float:
        return a / b

    func3(2, [2, 3])
    with open(os.path.join(path, "mylog.txt"), "r", encoding="utf-8") as f:
        err = f.read().split("\n")
    assert err[-2] == "func3 error: TypeError. Inputs: (2, [2, 3]), {}"


def test_log_err2() -> Any:
    @log(filename="mylog.txt")
    def func4(a: int) -> int:
        return int(a)

    func4("word")
    with open(os.path.join(path, "mylog.txt"), "r", encoding="utf-8") as f:
        err = f.read().split("\n")
    assert err[-2] == "func4 error: ValueError. Inputs: ('word',), {}"
