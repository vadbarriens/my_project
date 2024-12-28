import pytest
from typing import Any
from src.decorators import log, my_function


def test_log(capsys: Any) -> Any:
    @log(filename=None)
    def my_function() -> Any:
        captured = capsys.readouterr()
        assert captured.out == "my_function ok\n"
