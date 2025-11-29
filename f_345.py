from memoized import memoized

@memoized
def f(n: int) -> int:
    if n == 0:
        return 2
    if n < 0:
        return 3
    return 10 + f(n-1) + f(n-3) + f(n-5)

if __name__ == "__main__":
    print("| n | f(n) | Factor")
    print("| ---- | ---- | ---- |")
    for n in range(-5,90,5):
        print (f"| {n:3} | {f(n):,} | {f(n)/f(n-5):7.3} |")
