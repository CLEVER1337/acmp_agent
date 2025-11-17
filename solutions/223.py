
import sys
from collections import Counter
from functools import lru_cache

def solve() -> None:
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    S = data[0].strip()
    T = data[1].strip()
    n = len(S)

    if len(T) != n:
        print(0)
        return

    # quick impossibility test
    if Counter(S) != Counter(T):
        print(0)
        return

    sys.setrecursionlimit(10000)

    @lru_cache(maxsize=None)
    def dfs(i: int, stack: tuple) -> int:
        """
        i   – next unread position in S
        stack – tuple of characters, bottom … top
        returns number of ways to finish the transformation
        """
        j = i - len(stack)          # how many letters already written to output

        # finished ?
        if i == n and j == n:
            return 1

        ans = 0

        # 1) push next source letter
        if i < n:
            ans += dfs(i + 1, stack + (S[i],))

        # 2) pop if possible
        if stack and j < n and stack[-1] == T[j]:
            ans += dfs(i, stack[:-1])

        return ans

    print(dfs(0, tuple()))


if __name__ == '__main__':
    solve()
