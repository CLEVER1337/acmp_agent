
import sys

def solve() -> None:
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    N = int(data[0].strip())
    rows = [line.strip().split() for line in data[1:1 + N]]

    # pictures as N strings of length N
    front = [list(rows[i][0]) for i in range(N)]
    left =  [list(rows[i][1]) for i in range(N)]
    back =  [list(rows[i][2]) for i in range(N)]
    right = [list(rows[i][3]) for i in range(N)]
    top =   [list(rows[i][4]) for i in range(N)]
    bottom=[list(rows[i][5]) for i in range(N)]

    # emptiness flags for the three families of lines
    empty_z = [[False] * N for _ in range(N)]   # front / back direction
    for y in range(N):
        for x in range(N):
            i = N - 1 - y          # row index in front/back pictures
            j = x                  # column index
            if front[i][j] == '.' or back[i][j] == '.':
                empty_z[x][y] = True

    empty_x = [[False] * N for _ in range(N)]   # left / right direction
    for y in range(N):
        for z in range(N):
            i = N - 1 - y          # row index in left/right pictures
            j = z                  # column index
            if left[i][j] == '.' or right[i][j] == '.':
                empty_x[y][z] = True

    empty_y = [[False] * N for _ in range(N)]   # top / bottom direction
    for x in range(N):
        for z in range(N):
            i = z                  # row index in bottom picture
            j = x                  # column index
            if bottom[i][j] == '.' or top[i][j] == '.':
                empty_y[x][z] = True

    forced = 0
    for x in range(N):
        for y in range(N):
            for z in range(N):
                if empty_z[x][y] or empty_x[y][z] or empty_y[x][z]:
                    forced += 1

    answer = N * N * N - forced
    print(answer)


if __name__ == '__main__':
    solve()
