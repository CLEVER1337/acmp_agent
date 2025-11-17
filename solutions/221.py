
import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    K = int(next(it))          # allowed right turns
    N = int(next(it))          # rows
    M = int(next(it))          # columns

    grid = []
    start = None
    target = None
    for i in range(N):
        row = []
        for j in range(M):
            v = int(next(it))
            row.append(v)
            if v == 2:
                start = (i, j)
            elif v == 3:
                target = (i, j)
        grid.append(row)

    # trivial case
    if start == target:
        print(0)
        return

    # direction vectors: 0-up, 1-right, 2-down, 3-left
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # visited[x][y][dir][right_turns]
    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(M)] for _ in range(N)]
    q = deque()

    # first step from start – no turn is counted yet
    for d in range(4):
        nx = start[0] + dx[d]
        ny = start[1] + dy[d]
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 1:
            if not visited[nx][ny][d][0]:
                visited[nx][ny][d][0] = True
                q.append((nx, ny, d, 0, 1))

    while q:
        x, y, cur_dir, turns, steps = q.popleft()
        if (x, y) == target:
            print(steps)
            return

        for nxt_dir in range(4):
            nx = x + dx[nxt_dir]
            ny = y + dy[nxt_dir]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if grid[nx][ny] == 1:   # black cell – impassable
                continue

            # count a right turn if the new direction is clockwise from the current one
            inc = 1 if nxt_dir == (cur_dir + 1) % 4 else 0
            new_turns = turns + inc
            if new_turns > K:
                continue
            if not visited[nx][ny][nxt_dir][new_turns]:
                visited[nx][ny][nxt_dir][new_turns] = True
                q.append((nx, ny, nxt_dir, new_turns, steps + 1))

    # target unreachable
    print(-1)

if __name__ == '__main__':
    solve()
