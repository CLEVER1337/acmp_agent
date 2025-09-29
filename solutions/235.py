
def main():
    with open("INPUT.TXT", "r") as f:
        program = f.readline().strip()
    
    x, y = 0, 0
    visited = {(0, 0): True}
    direction = 0  # 0: вверх, 1: вправо, 2: вниз, 3: влево
    steps = 0
    
    for cmd in program:
        if cmd == 'S':
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            steps += 1
            
            if (x, y) in visited:
                with open("OUTPUT.TXT", "w") as f:
                    f.write(str(steps))
                return
            visited[(x, y)] = True
            
        elif cmd == 'R':
            direction = (direction + 1) % 4
        elif cmd == 'L':
            direction = (direction - 1) % 4
    
    with open("OUTPUT.TXT", "w") as f:
        f.write("-1")

if __name__ == "__main__":
    main()
