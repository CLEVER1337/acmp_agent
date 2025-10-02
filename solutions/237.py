
def main():
    import sys
    sys.setrecursionlimit(10000)
    
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i]))
    
    words = []
    for i in range(1 + n, 1 + n + m):
        words.append(data[i])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(x, y, word, index, visited):
        if index == len(word):
            return True
        
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        
        if visited[x][y] or grid[x][y] != word[index]:
            return False
        
        visited[x][y] = True
        for dx, dy in directions:
            if dfs(x + dx, y + dy, word, index + 1, visited):
                return True
        visited[x][y] = False
        return False
    
    def find_word(word):
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == word[0]:
                    if dfs(i, j, word, 0, visited):
                        return True
        return False
    
    def remove_word(word):
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == word[0]:
                    if dfs(i, j, word, 0, visited):
                        for x in range(n):
                            for y in range(n):
                                if visited[x][y]:
                                    grid[x][y] = '.'
                        return True
        return False
    
    for word in words:
        remove_word(word)
    
    result = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != '.':
                result.append(grid[i][j])
    
    result.sort()
    print(''.join(result))

if __name__ == '__main__':
    main()
