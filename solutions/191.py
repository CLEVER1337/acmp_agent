
import sys
import math

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])

    # ---- find the length L of the N-th smooth number ----
    L = 0
    total = 0            # total amount of smooth numbers with length <= L
    while total < N:
        L += 1
        # count of smooth numbers with exactly length L:
        total = math.comb(L + 9, 9) - 1   # C(L+9,9) - 1

    # numbers with length < L
    prev_total = math.comb(L + 8, 9) - 1   # C(L+8,9) - 1
    offset = N - prev_total - 1           # 0‑based index inside the block of length L

    # ---- construct the offset‑th non‑decreasing sequence of length L ----
    digits = []
    cur_min = 1
    rem = L  # how many positions are still to fill
    while rem:
        for d in range(cur_min, 10):
            # number of completions when current digit is d
            cnt = math.comb((rem - 1) + (9 - d), rem - 1)
            if offset < cnt:
                digits.append(str(d))
                cur_min = d
                rem -= 1
                break
            offset -= cnt

    sys.stdout.write(''.join(digits))


if __name__ == "__main__":
    solve()
