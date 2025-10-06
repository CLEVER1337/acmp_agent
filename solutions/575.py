
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
    
    total_length = 0.0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(n):
        for j in range(m):
            current_room = grid[i][j]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] != current_room:
                        total_length += 1
                else:
                    total_length += 1
    
    wall_thickness = 0.2
    wall_height = 3.0
    volume = total_length * wall_thickness * wall_height
    print("{:.3f}".format(volume))

if __name__ == "__main__":
    main()
