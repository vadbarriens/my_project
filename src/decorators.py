import os
from functools import wraps
from typing import Any, Callable, Optional
from config import path


def log(filename: Optional[str]) -> Callable:
    """Декоратор, который записывает логи работы функций"""

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(os.path.join(path, "mylog.txt"), "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(os.path.join(path, "mylog.txt"), "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")


        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """суммирует два значения"""
    return x + y


my_function(3, 2)
