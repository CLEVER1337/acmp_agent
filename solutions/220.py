
import sys

def ceil_div(a: int, b: int) -> int:
    """ceil(a / b) for b > 0, works for negative a as well."""
    return -((-a) // b)


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    U = next(it)          # screen height
    H = next(it)          # cursor height
    T = next(it)          # scroll step
    L = next(it)          # table height
    N = next(it)          # number of lines
    X = [next(it) for _ in range(N)]

    max_y = U - H                     # biggest possible top of cursor

    # number of performed scroll steps (see formula (2))
    if L <= U:
        K = 0
    else:
        K = (L - U + T - 1) // T      # ceil((L-U)/T)

    # occ[s] – how many line appearances happen on screen row s
    occ = [0] * U

    # local copies for speed
    U_minus_1 = U - 1
    T_val = T
    K_val = K
    H_val = H
    occ_local = occ          # alias

    for xi in X:
        # first scroll step where the line can be visible
        k_start = ceil_div(xi - U_minus_1, T_val)
        if k_start < 0:
            k_start = 0
        # last scroll step where the line can be visible
        k_end = xi // T_val
        if k_end > K_val:
            k_end = K_val
        if k_start > k_end:
            continue                # line never appears

        # first screen row of this line
        s = xi - k_start * T_val
        m = k_end - k_start + 1      # number of appearances

        # add all its appearances
        for _ in range(m):
            occ_local[s] += 1
            s -= T_val               # next screen row (decreasing)

    # sliding window of size H over occ[]
    cur = sum(occ[:H])
    ans = cur
    for y in range(1, max_y + 1):
        cur += occ[y + H - 1] - occ[y - 1]
        if cur < ans:
            ans = cur

    sys.stdout.write(str(ans))


if __name__ == '__main__':
    solve()
