
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    if N == 1:
        ans = 1
    else:
        ans = N * (N - 1)
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    solve()
