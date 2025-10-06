
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    min_i = n
    max_i = -1
    min_j = m
    max_j = -1
    black_count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                black_count += 1
                if i < min_i:
                    min_i = i
                if i > max_i:
                    max_i = i
                if j < min_j:
                    min_j = j
                if j > max_j:
                    max_j = j
    
    if min_i == n:
        print("SQUARE")
        return
        
    height = max_i - min_i + 1
    width = max_j - min_j + 1
    
    if height < 3 or width < 3:
        print("CIRCLE")
        return
        
    expected_black = height * width - (height - 2) * (width - 2)
    
    if black_count > expected_black:
        print("CIRCLE")
        return
        
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if i == min_i or i == max_i or j == min_j or j == max_j:
                if grid[i][j] != '*':
                    print("CIRCLE")
                    return
            else:
                if grid[i][j] == '*':
                    print("CIRCLE")
                    return
                    
    print("SQUARE")

if __name__ == "__main__":
    main()
