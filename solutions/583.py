
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    commands = []
    for i in range(1, n + 1):
        parts = data[i].split()
        if parts[0] == 'forward':
            commands.append(('forward', int(parts[1])))
        elif parts[0] == 'left':
            commands.append(('left',))
        elif parts[0] == 'right':
            commands.append(('right',))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0
    x, y = 0, 0
    points = [(0, 0)]
    
    for cmd in commands:
        if cmd[0] == 'forward':
            dist = cmd[1]
            dx, dy = directions[current_dir]
            x += dx * dist
            y += dy * dist
            points.append((x, y))
        elif cmd[0] == 'left':
            current_dir = (current_dir - 1) % 4
        elif cmd[0] == 'right':
            current_dir = (current_dir + 1) % 4
    
    if points[0] != points[-1]:
        print("FALSE")
        return
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    segments = []
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        segments.append((p1, p2))
    
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            s1 = segments[i]
            s2 = segments[j]
            
            if s1[0][0] == s1[1][0]:
                vertical = s1
                horizontal = s2
                if horizontal[0][1] != horizontal[1][1]:
                    continue
            elif s1[0][1] == s1[1][1]:
                horizontal = s1
                vertical = s2
                if vertical[0][0] != vertical[1][0]:
                    continue
            else:
                continue
                
            if horizontal[0][1] != vertical[0][1] and horizontal[0][1] != vertical[1][1]:
                continue
            if vertical[0][0] != horizontal[0][0] and vertical[0][0] != horizontal[1][0]:
                continue
            
            hx1, hx2 = sorted([horizontal[0][0], horizontal[1][0]])
            hy = horizontal[0][1]
            vx = vertical[0][0]
            vy1, vy2 = sorted([vertical[0][1], vertical[1][1]])
            
            if hx1 <= vx <= hx2 and vy1 <= hy <= vy2:
                found = False
                for seg in segments:
                    p1, p2 = seg
                    if p1[0] == p2[0]:
                        seg_x = p1[0]
                        seg_y1, seg_y2 = sorted([p1[1], p2[1]])
                        if seg_x == vx and seg_y1 <= hy <= seg_y2:
                            found = True
                            break
                    elif p1[1] == p2[1]:
                        seg_y = p1[1]
                        seg_x1, seg_x2 = sorted([p1[0], p2[0]])
                        if seg_y == hy and seg_x1 <= vx <= seg_x2:
                            found = True
                            break
                
                if not found:
                    print("FALSE")
                    return
    
    print("TRUE")

if __name__ == "__main__":
    main()
