
def main():
    import sys
    from collections import deque
    
    data = sys.stdin.read().splitlines()
    if not data:
        print("")
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i].strip()))
    
    words = []
    for i in range(1 + n, 1 + n + m):
        words.append(data[i].strip())
    
    total_letters = sum(len(word) for word in words)
    found_count = 0
    marked = [[False] * n for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for word in words:
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == word[0] and not marked[i][j]:
                    stack = deque()
                    stack.append((i, j, 0, []))
                    while stack and not found:
                        x, y, idx, path = stack.pop()
                        if idx == len(word) - 1:
                            if grid[x][y] == word[idx]:
                                for px, py in path:
                                    marked[px][py] = True
                                marked[x][y] = True
                                found = True
                                break
                            continue
                        
                        if grid[x][y] != word[idx]:
                            continue
                            
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and not marked[nx][ny]:
                                stack.append((nx, ny, idx + 1, path + [(x, y)]))
    
    result = []
    for i in range(n):
        for j in range(n):
            if not marked[i][j]:
                result.append(grid[i][j])
                
    result.sort()
    print(''.join(result))

if __name__ == "__main__":
    main()
