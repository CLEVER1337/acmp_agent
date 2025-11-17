
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])

    # number of street segments
    edges = 2 * N * M + N + M

    # minimal additional length (extra)
    if N % 2 == 1 and M % 2 == 1:                 # both odd
        extra = N + M - 2
    elif N % 2 == 1 and M % 2 == 0:                # N odd, M even
        extra = 2 * N + M - 3
    elif N % 2 == 0 and M % 2 == 1:                # N even, M odd
        extra = N + 2 * M - 3
    else:                                          # both even
        extra = N + M

    answer = edges + extra
    sys.stdout.write(str(answer))

if __name__ == '__main__':
    solve()
