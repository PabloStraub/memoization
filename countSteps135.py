def count_steps_135(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_steps_135(n - 1) + count_steps_135(n - 3) + count_steps_135(n - 5)

if __name__ == "__main__":
    print(f"{count_steps_135(4)=}")
    print(f"{count_steps_135(10)=}")
    print(f"{count_steps_135(20)=}")
    print(f"{count_steps_135(30)=}")
    print(f"{count_steps_135(35)=}")
    print(f"{count_steps_135(38)=}")
    print(f"{count_steps_135(40)=}")