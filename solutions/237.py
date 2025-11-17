
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("")
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1+n):
        grid.append(list(data[i].strip()))
    
    words = []
    for i in range(1+n, 1+n+m):
        words.append(data[i].strip())
    
    total_letters = []
    for row in grid:
        total_letters.extend(row)
    
    from collections import Counter
    total_count = Counter(total_letters)
    
    used_count = Counter()
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def dfs(x, y, word, index, visited):
        if index == len(word):
            return True
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        if visited[x][y]:
            return False
        if grid[x][y] != word[index]:
            return False
            
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if dfs(nx, ny, word, index+1, visited):
                return True
        visited[x][y] = False
        return False
        
    def find_word(word):
        for i in range(n):
            for j in range(n):
                visited = [[False]*n for _ in range(n)]
                if dfs(i, j, word, 0, visited):
                    for x in range(n):
                        for y in range(n):
                            if visited[x][y]:
                                used_count[grid[x][y]] += 1
                    return
        return
    
    for word in words:
        find_word(word)
        
    remaining = []
    for char in total_count:
        count_remaining = total_count[char] - used_count[char]
        remaining.extend([char] * count_remaining)
        
    remaining.sort()
    print(''.join(remaining))

if __name__ == "__main__":
    main()
