
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
    
    total_length = 0
    for i in range(n):
        for j in range(m):
            current_room = grid[i][j]
            
            if i > 0 and grid[i-1][j] != current_room:
                total_length += 1
            
            if i < n-1 and grid[i+1][j] != current_room:
                total_length += 1
            
            if j > 0 and grid[i][j-1] != current_room:
                total_length += 1
            
            if j < m-1 and grid[i][j+1] != current_room:
                total_length += 1
    
    wall_thickness = 0.2
    wall_height = 3.0
    volume = total_length * wall_thickness * wall_height
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.3f}".format(volume))

if __name__ == "__main__":
    main()
