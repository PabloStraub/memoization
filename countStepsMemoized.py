from typing import Iterable
from memoized import memoized

@memoized
def count_steps(n: int, steps: Iterable[int]) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(count_steps(n - step, steps) for step in steps)

if __name__ == "__main__":
    print(f"{count_steps(10, (1,3,5))=}")
    print(f"{count_steps(20, (1,3,5))=}")
    print(f"{count_steps(30, (1,3,5))=}")
    print(f"{count_steps(35, (1,3,5))=}")
    print(f"{count_steps(38, (1,3,5))=}")
    print(f"{count_steps(100, (1,3,5))=}")