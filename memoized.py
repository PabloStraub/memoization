# @memoized is a generic decorator for pure functions with any number of parameters

from typing import Callable

def memoized(func: Callable) -> Callable:
    memo: dict = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper
