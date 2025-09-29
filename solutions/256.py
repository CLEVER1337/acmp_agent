
def main():
    directions = {'X': (1, -1, 0), 'Y': (0, 1, -1), 'Z': (-1, 0, 1)}
    
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        x, y, z = 0, 0, 0
        
        for _ in range(n):
            line = f.readline().split()
            direction = line[0]
            steps = int(line[1])
            
            dx, dy, dz = directions[direction]
            x += dx * steps
            y += dy * steps
            z += dz * steps
    
    distance = (abs(x) + abs(y) + abs(z)) // 2
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(distance))

if __name__ == '__main__':
    main()
