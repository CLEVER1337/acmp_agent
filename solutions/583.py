
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    commands = []
    for i in range(1, n + 1):
        parts = data[i].split()
        if parts[0] == 'forward':
            commands.append(('f', int(parts[1])))
        elif parts[0] == 'left':
            commands.append(('l',))
        elif parts[0] == 'right':
            commands.append(('r',))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    x, y = 0, 0
    points = [(x, y)]
    
    for cmd in commands:
        if cmd[0] == 'f':
            dist = cmd[1]
            dx, dy = directions[dir_idx]
            x += dx * dist
            y += dy * dist
            points.append((x, y))
        elif cmd[0] == 'l':
            dir_idx = (dir_idx - 1) % 4
        elif cmd[0] == 'r':
            dir_idx = (dir_idx + 1) % 4
    
    if points[0] != points[-1]:
        print("FALSE")
        return
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    vertical_segments = []
    horizontal_segments = []
    
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        if x1 == x2:
            vertical_segments.append((x1, min(y1, y2), max(y1, y2)))
        else:
            horizontal_segments.append((y1, min(x1, x2), max(x1, x2)))
    
    for seg in vertical_segments:
        x, y_min, y_max = seg
        for test_y in range(y_min + 1, y_max):
            found = False
            for h_seg in horizontal_segments:
                y, x_min, x_max = h_seg
                if y == test_y and x_min <= x <= x_max:
                    found = True
                    break
            if not found:
                print("FALSE")
                return
    
    for seg in horizontal_segments:
        y, x_min, x_max = seg
        for test_x in range(x_min + 1, x_max):
            found = False
            for v_seg in vertical_segments:
                x, y_min, y_max = v_seg
                if x == test_x and y_min <= y <= y_max:
                    found = True
                    break
            if not found:
                print("FALSE")
                return
    
    print("TRUE")

if __name__ == "__main__":
    main()
