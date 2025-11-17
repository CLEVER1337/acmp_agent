
import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n = int(data[0].strip())
    # read the map
    grid = [list(line.rstrip()) for line in data[1:1 + n]]

    # 4 directions: up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # ------------------------------------------------------------
    # 1) find all empty cells reachable from the two entrances
    visited = [[False] * n for _ in range(n)]
    q = deque()

    # both corners are guaranteed to be empty
    visited[0][0] = True
    q.append((0, 0))
    visited[n - 1][n - 1] = True
    q.append((n - 1, n - 1))

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    # ------------------------------------------------------------
    # 2) count every visible wall side (25 m^2 per side)
    cnt = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                continue
            for d, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # interior wall side
                    if grid[nr][nc] == '#':
                        cnt += 1
                else:
                    # side that goes out of the grid → outer wall
                    opening = False
                    # openings are only the four sides of the two corner cells
                    if r == 0 and c == 0 and d == 0:          # top side of (0,0)
                        opening = True
                    if r == 0 and c == 0 and d == 3:          # left side of (0,0)
                        opening = True
                    if r == n - 1 and c == n - 1 and d == 2:   # bottom side of (n‑1,n‑1)
                        opening = True
                    if r == n - 1 and c == n - 1 and d == 1:   # right side of (n‑1,n‑1)
                        opening = True
                    if not opening:
                        cnt += 1

    area = cnt * 25          # 5 m × 5 m side
    print(area)


if __name__ == '__main__':
    solve()
