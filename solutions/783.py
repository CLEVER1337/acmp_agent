
def main():
    grid = []
    for _ in range(8):
        line = input().strip()
        grid.append(line)
    
    count = 0
    for i in range(8):
        for j in range(8):
            expected_color = 'W' if (i + j) % 2 == 0 else 'B'
            if grid[i][j] != expected_color:
                count += 1
    
    print(min(count, 64 - count))

if __name__ == "__main__":
    main()
