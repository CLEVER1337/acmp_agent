
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        grid.append(row)
    
    max_sum = -10**18
    
    for i in range(n):
        for j in range(n):
            current = grid[i][j]
            
            if i > 0:
                top = grid[i-1][j]
                if i > 1:
                    max_sum = max(max_sum, current + top + grid[i-2][j])
                if j > 0:
                    max_sum = max(max_sum, current + top + grid[i-1][j-1])
                if j < n-1:
                    max_sum = max(max_sum, current + top + grid[i-1][j+1])
            
            if i < n-1:
                bottom = grid[i+1][j]
                if i < n-2:
                    max_sum = max(max_sum, current + bottom + grid[i+2][j])
                if j > 0:
                    max_sum = max(max_sum, current + bottom + grid[i+1][j-1])
                if j < n-1:
                    max_sum = max(max_sum, current + bottom + grid[i+1][j+1])
            
            if j > 0:
                left = grid[i][j-1]
                if j > 1:
                    max_sum = max(max_sum, current + left + grid[i][j-2])
                if i > 0:
                    max_sum = max(max_sum, current + left + grid[i-1][j-1])
                if i < n-1:
                    max_sum = max(max_sum, current + left + grid[i+1][j-1])
            
            if j < n-1:
                right = grid[i][j+1]
                if j < n-2:
                    max_sum = max(max_sum, current + right + grid[i][j+2])
                if i > 0:
                    max_sum = max(max_sum, current + right + grid[i-1][j+1])
                if i < n-1:
                    max_sum = max(max_sum, current + right + grid[i+1][j+1])
    
    print(max_sum)

if __name__ == "__main__":
    main()
