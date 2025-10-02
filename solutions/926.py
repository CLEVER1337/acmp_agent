
def main():
    import sys
    sys.setrecursionlimit(10000)
    
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i]))
    
    cities = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'C':
                cities.append((i, j))
    
    total_cities = len(cities)
    required = total_cities // 2
    
    result = [[0] * n for _ in range(n)]
    
    def dfs(i, j, state):
        if i < 0 or i >= n or j < 0 or j >= n:
            return 0
        if result[i][j] != 0:
            return 0
        if grid[i][j] == 'C':
            if state == 1 and required > 0:
                result[i][j] = 1
                required -= 1
                return 1
            else:
                result[i][j] = 2
                return 0
        else:
            result[i][j] = state
            return 0
    
    count1 = 0
    for i in range(n):
        for j in range(n):
            if result[i][j] == 0:
                count1 += dfs(i, j, 1)
                if count1 >= required:
                    break
        if count1 >= required:
            break
    
    for i in range(n):
        for j in range(n):
            if result[i][j] == 0:
                dfs(i, j, 2)
    
    output_lines = []
    for i in range(n):
        output_lines.append(''.join(str(x) for x in result[i]))
    
    sys.stdout.write('\n'.join(output_lines))

if __name__ == "__main__":
    main()
