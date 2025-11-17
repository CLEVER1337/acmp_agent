
import sys
import bisect

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    M = next(it)
    W = [0] * M
    E = [0] * M
    for i in range(M):
        W[i] = next(it)
        E[i] = next(it)
    N = next(it)
    pos = [0] * N
    for i in range(N):
        pos[i] = next(it)

    # pos are given sorted, but sorting does not hurt
    # pos.sort()

    # dp[i][t] – maximum number of trees ending at position i with type t
    dp = [[0] * M for _ in range(N)]
    # prefix[s][i] – max dp[0..i][s]
    prefix = [[0] * N for _ in range(M)]

    for i in range(N):
        xi = pos[i]
        for t in range(M):
            best = 1                     # start new tree at this position
            Wt = W[t]
            for s in range(M):
                # required distance between previous tree of type s and current tree of type t
                th = E[s]
                if th < Wt:
                    th = Wt
                limit = xi - th
                # find rightmost previous position j < i with pos[j] <= limit
                idx = bisect.bisect_right(pos, limit, 0, i) - 1
                if idx >= 0:
                    cand = prefix[s][idx] + 1
                    if cand > best:
                        best = cand
            dp[i][t] = best
        # update prefix tables for all types
        for s in range(M):
            if i == 0:
                prefix[s][i] = dp[i][s]
            else:
                prev = prefix[s][i - 1]
                cur = dp[i][s]
                prefix[s][i] = cur if cur > prev else prev

    answer = 0
    for i in range(N):
        row_max = max(dp[i])
        if row_max > answer:
            answer = row_max
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    solve()
