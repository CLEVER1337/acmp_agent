
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    N, M = data[0], data[1]
    pos = 2

    # configuration after all moves
    cur = data[pos:pos + N]
    pos += N

    # recorded last boxes for moves 1..M (1‑based)
    last_boxes = data[pos:pos + M]

    # reverse all moves
    for move in range(M - 1, -1, -1):
        last = last_boxes[move]          # 1‑based
        last0 = last - 1                 # 0‑based

        found = False
        for s in range(N):               # try every possible source
            t = cur[s]                    # cur[s] == K // N
            r = (last0 - s) % N           # remainder K % N
            # check condition (4)
            ok = True
            for i in range(N):
                if i == s:
                    continue
                offset = (i - s) % N
                extra = 1 if (1 <= offset <= r) else 0
                if cur[i] < t + extra:
                    ok = False
                    break
            if not ok:
                continue

            # all requirements satisfied – rebuild previous configuration
            pre = [0] * N
            pre[s] = r + t * N            # K
            for i in range(N):
                if i == s:
                    continue
                offset = (i - s) % N
                extra = 1 if (1 <= offset <= r) else 0
                pre[i] = cur[i] - t - extra
            cur = pre
            found = True
            break

        if not found:
            # According to the statement this never happens.
            raise RuntimeError("No valid source found for a move")

    sys.stdout.write(' '.join(str(x) for x in cur))

if __name__ == '__main__':
    solve()
