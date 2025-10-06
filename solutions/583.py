
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    commands = []
    for i in range(1, n + 1):
        line = data[i].strip()
        if line.startswith('forward'):
            parts = line.split()
            commands.append(('forward', int(parts[1])))
        elif line.startswith('left'):
            commands.append(('left',))
        elif line.startswith('right'):
            commands.append(('right',))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    points = [(x, y)]
    dir_index = 0
    
    for cmd in commands:
        if cmd[0] == 'forward':
            dist = cmd[1]
            dx, dy = directions[dir_index]
            x += dx * dist
            y += dy * dist
            points.append((x, y))
        elif cmd[0] == 'left':
            dir_index = (dir_index - 1) % 4
        elif cmd[0] == 'right':
            dir_index = (dir_index + 1) % 4
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    def is_inside(x, y):
        if x < min_x or x > max_x or y < min_y or y > max_y:
            return False
        count = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            if y1 == y2:
                if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                    return True
            else:
                if min(y1, y2) <= y <= max(y1, y2):
                    if x1 == x2:
                        if x <= x1:
                            count += 1
                    else:
                        if x <= x1 + (x2 - x1) * (y - y1) / (y2 - y1):
                            count += 1
        return count % 2 == 1
    
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        if x1 == x2:
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                if not is_inside(x1, y):
                    print("FALSE")
                    return
        elif y1 == y2:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                if not is_inside(x, y1):
                    print("FALSE")
                    return
    
    print("TRUE")

if __name__ == "__main__":
    main()
