
import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    s = data[2].strip()

    INF = N + 5
    dp = [0] * N

    # monotonic deques: each element is (index, dp_value)
    global_dq = deque()
    char_deqs = [deque() for _ in range(26)]

    # initial position 0
    dp[0] = 0
    # insert into global
    while global_dq and global_dq[-1][1] >= dp[0]:
        global_dq.pop()
    global_dq.append((0, dp[0]))
    # insert into its character deque
    idx0 = ord(s[0]) - 65
    while char_deqs[idx0] and char_deqs[idx0][-1][1] >= dp[0]:
        char_deqs[idx0].pop()
    char_deqs[idx0].append((0, dp[0]))

    for j in range(1, N):
        bound = j - K

        # remove outdated entries from global deque
        while global_dq and global_dq[0][0] < bound:
            global_dq.popleft()
        # remove outdated entries from all character deques
        for dq in char_deqs:
            while dq and dq[0][0] < bound:
                dq.popleft()

        idx = ord(s[j]) - 65

        # minimal cost when landing on a same character
        min_same = char_deqs[idx][0][1] if char_deqs[idx] else INF
        # minimal cost among all previous positions
        min_any = global_dq[0][1] if global_dq else INF

        # compute dp[j]
        # 0‑cost jump if characters equal, otherwise 1‑cost
        if min_same <= min_any + 1:
            dp[j] = min_same
        else:
            dp[j] = min_any + 1

        # insert dp[j] into global deque (maintain monotonicity)
        while global_dq and global_dq[-1][1] >= dp[j]:
            global_dq.pop()
        global_dq.append((j, dp[j]))

        # insert into its character deque (maintain monotonicity)
        while char_deqs[idx] and char_deqs[idx][-1][1] >= dp[j]:
            char_deqs[idx].pop()
        char_deqs[idx].append((j, dp[j]))

    sys.stdout.write(str(dp[N - 1]))

if __name__ == "__main__":
    solve()
