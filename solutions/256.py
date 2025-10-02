
def main():
    n = int(input().strip())
    x, y, z = 0, 0, 0
    
    for _ in range(n):
        line = input().split()
        direction = line[0]
        steps = int(line[1])
        
        if direction == 'X':
            x += steps
        elif direction == 'Y':
            y += steps
        elif direction == 'Z':
            z += steps
    
    dx = abs(x)
    dy = abs(y)
    dz = abs(z)
    
    if (x >= 0 and y >= 0 and z >= 0) or (x <= 0 and y <= 0 and z <= 0):
        result = max(dx, dy, dz)
    else:
        result = dx + dy + dz - max(dx, dy, dz)
    
    print(result)

if __name__ == "__main__":
    main()
