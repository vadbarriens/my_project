from functools import wraps
from typing import Optional, Callable


def log(filename: Optional[str]) -> Callable:
    """Декоратор, который записывает логи работы функций"""
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                raise e
        return wrapper
    return my_decorator


@log(filename='mylog.txt')
def my_function(x: int, y: int) -> int:
    """ суммирует два значения """
    return x+y


my_function('3', 3)
