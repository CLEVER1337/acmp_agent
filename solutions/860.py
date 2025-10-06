
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
    
    total = n * m
    if total > 100:
        print(0)
        return
        
    dp = {}
    mask = [0] * m
    
    def get_state():
        return tuple(mask)
    
    def dfs(i, j):
        if j == m:
            return dfs(i + 1, 0)
        if i == n:
            return 1
            
        key = (i, j, get_state())
        if key in dp:
            return dp[key]
            
        if grid[i][j] == '#':
            res = dfs(i, j + 1)
            dp[key] = res
            return res
            
        res = 0
        if mask[j] == 0:
            if j + 1 < m and mask[j + 1] == 0 and grid[i][j + 1] == '.':
                mask[j] = mask[j + 1] = 1
                res += dfs(i, j + 2)
                mask[j] = mask[j + 1] = 0
                
            if i + 1 < n and grid[i + 1][j] == '.':
                mask[j] = 1
                res += dfs(i, j + 1)
                mask[j] = 0
        else:
            res = dfs(i, j + 1)
            
        dp[key] = res
        return res
        
    result = dfs(0, 0)
    print(result)

if __name__ == "__main__":
    main()
