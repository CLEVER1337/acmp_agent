
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    if n == 0 or m == 0:
        print(0)
        return
        
    size = n * m
    dp = [0] * (1 << size)
    dp[0] = 1
    
    for mask in range(1 << size):
        if dp[mask] == 0:
            continue
            
        pos = 0
        while pos < size and (mask & (1 << pos)):
            pos += 1
            
        if pos >= size:
            continue
            
        i, j = pos // m, pos % m
        if grid[i][j] == '#':
            continue
            
        if j + 1 < m and i < n and not (mask & (1 << pos)) and not (mask & (1 << (pos + 1))) and grid[i][j] == '.' and grid[i][j+1] == '.':
            new_mask = mask | (1 << pos) | (1 << (pos + 1))
            dp[new_mask] += dp[mask]
            
        if i + 1 < n and j < m and not (mask & (1 << pos)) and not (mask & (1 << (pos + m))) and grid[i][j] == '.' and grid[i+1][j] == '.':
            new_mask = mask | (1 << pos) | (1 << (pos + m))
            dp[new_mask] += dp[mask]
            
    print(dp[(1 << size) - 1])

if __name__ == "__main__":
    main()
