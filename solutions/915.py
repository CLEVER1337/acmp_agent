
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
    
    if n == 1 and m == 1:
        print(6 * grid[0][0])
        return
        
    dp = [[[-10**18] * 6 for _ in range(m)] for __ in range(n)]
    
    top_faces = {
        0: [1, 2, 3, 4, 5],
        1: [0, 2, 4, 5, 3],
        2: [0, 1, 3, 5, 4],
        3: [0, 2, 4, 5, 1],
        4: [0, 1, 3, 5, 2],
        5: [1, 2, 3, 4, 0]
    }
    
    dp[0][0][0] = 6 * grid[0][0]
    
    for i in range(n):
        for j in range(m):
            for top in range(6):
                if dp[i][j][top] == -10**18:
                    continue
                    
                current_val = dp[i][j][top]
                
                if i + 1 < n:
                    for next_top in top_faces[top]:
                        new_val = current_val + 6 * grid[i+1][j]
                        if new_val > dp[i+1][j][next_top]:
                            dp[i+1][j][next_top] = new_val
                
                if j + 1 < m:
                    for next_top in top_faces[top]:
                        new_val = current_val + 6 * grid[i][j+1]
                        if new_val > dp[i][j+1][next_top]:
                            dp[i][j+1][next_top] = new_val
    
    result = max(dp[n-1][m-1])
    print(result)

if __name__ == "__main__":
    main()
