
def main():
    with open("INPUT.TXT", "r") as f:
        n, m = map(int, f.readline().split())
        y, x = map(int, f.readline().split())
    
    field = [[1] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    i, j = 0, 0
    total_berries = 0
    
    while True:
        if not visited[i][j]:
            total_berries += field[i][j]
            visited[i][j] = True
        
        if i + 1 == y and j + 1 == x:
            break
            
        next_i = i + directions[dir_idx][0]
        next_j = j + directions[dir_idx][1]
        
        if (0 <= next_i < n and 0 <= next_j < m and 
            not visited[next_i][next_j]):
            i, j = next_i, next_j
        else:
            dir_idx = (dir_idx + 1) % 4
            next_i = i + directions[dir_idx][0]
            next_j = j + directions[dir_idx][1]
            if 0 <= next_i < n and 0 <= next_j < m:
                i, j = next_i, next_j
            else:
                break
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(total_berries))

if __name__ == "__main__":
    main()
