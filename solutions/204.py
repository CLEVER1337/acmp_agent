
import sys

def prefix_function(s: str):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def solve() -> None:
    data = sys.stdin.read().strip()
    if not data:
        print(0)
        return
    s = data
    n = len(s)
    pi = prefix_function(s)
    # minimal period length
    period = n - pi[-1]
    print(period)

if __name__ == '__main__':
    solve()
