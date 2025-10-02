
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(data[i].strip()))
    
    if n == 0 or m == 0:
        print(0)
        return
        
    size_lim = min(n, m)
    ways = 0
    
    for size in range(1, size_lim + 1):
        valid = True
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                square_valid = True
                for di in range(size):
                    for dj in range(size):
                        if grid[i + di][j + dj] != '.':
                            square_valid = False
                            break
                    if not square_valid:
                        break
                if square_valid:
                    ways += 1
                    
    print(ways)

if __name__ == "__main__":
    main()
