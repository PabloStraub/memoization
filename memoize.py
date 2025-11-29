from typing import Callable, TypeVar, Dict

T = TypeVar("T")
R = TypeVar("R")

def memoize(func: Callable[[T,list[T]], R]) -> Callable[[T,list[T]], R]:
    memo: Dict[T, R] = {}

    def wrapper(arg: T, arg2: list[T]) -> R:
        if arg in memo:
            return memo[arg]
        result = func(arg, arg2)
        memo[arg] = result
        return result

    return wrapper
