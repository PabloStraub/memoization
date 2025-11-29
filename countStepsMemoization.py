def count_steps(n: int, steps: list[int], memo: dict[int,int]) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    result = sum(count_steps(n - step, steps, memo) for step in steps)
    memo[n] = result
    return result

if __name__ == "__main__":
    print(f"{count_steps(10, [1,3,5], {})=}")
    print(f"{count_steps(20, [1,3,5], {})=}")
    print(f"{count_steps(30, [1,3,5], {})=}")
    print(f"{count_steps(35, [1,3,5], {})=}")
    print(f"{count_steps(38, [1,3,5], {})=}")
    print(f"{count_steps(300, [1,3,5], {})=}")