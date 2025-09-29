
def main():
    with open('INPUT.TXT', 'r') as f:
        path = f.readline().strip()
    
    x, y = 0, 0
    visited = {(0, 0)}
    
    for move in path:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        visited.add((x, y))
    
    cx, cy = x, y
    result = []
    priority = ['N', 'E', 'S', 'W']
    dx = {'N': 0, 'S': 0, 'E': 1, 'W': -1}
    dy = {'N': 1, 'S': -1, 'E': 0, 'W': 0}
    
    while cx != 0 or cy != 0:
        for direction in priority:
            nx = cx + dx[direction]
            ny = cy + dy[direction]
            if (nx, ny) in visited:
                result.append(direction)
                cx, cy = nx, ny
                break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(result))

if __name__ == '__main__':
    main()
