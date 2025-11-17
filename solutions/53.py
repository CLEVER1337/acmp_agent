
import sys

def solve() -> None:
    """
    Reads n and m, counts colors in the multiplication table according to the
    described painting order and prints the results.

    Colors (priority from highest to lowest):
        BLUE  – numbers divisible by 5
        GREEN – numbers divisible by 3 but not by 5
        RED   – even numbers that are not divisible by 3 or 5
        BLACK – all remaining numbers
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m = map(int, data[:2])

    red = green = blue = black = 0

    # Direct enumeration – at most 10⁶ iterations for the given limits.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prod = i * j
            if prod % 5 == 0:
                blue += 1
            elif prod % 3 == 0:
                green += 1
            elif prod % 2 == 0:
                red += 1
            else:
                black += 1

    out_lines = [
        f"RED : {red}",
        f"GREEN : {green}",
        f"BLUE : {blue}",
        f"BLACK : {black}"
    ]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
