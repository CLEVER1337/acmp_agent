
def main():
    import sys
    from collections import deque
    
    data = sys.stdin.read().split()
    if not data:
        return
    
    W = int(data[0])
    H = int(data[1])
    n = int(data[2])
    
    segments = []
    index = 3
    for i in range(n):
        a, b, c, d = map(int, data[index:index+4])
        index += 4
        segments.append((min(a, c), min(b, d), max(a, c), max(b, d)))
    
    vertical_segments = []
    horizontal_segments = []
    
    for seg in segments:
        x1, y1, x2, y2 = seg
        if x1 == x2:
            vertical_segments.append((x1, y1, y2))
        elif y1 == y2:
            horizontal_segments.append((y1, x1, x2))
    
    vertical_segments.sort(key=lambda x: x[0])
    horizontal_segments.sort(key=lambda x: x[0])
    
    x_lines = sorted(set([0, W] + [x for x, _, _ in vertical_segments]))
    y_lines = sorted(set([0, H] + [y for y, _, _ in horizontal_segments]))
    
    areas = []
    visited = set()
    
    for i in range(len(x_lines) - 1):
        for j in range(len(y_lines) - 1):
            x_start, x_end = x_lines[i], x_lines[i + 1]
            y_start, y_end = y_lines[j], y_lines[j + 1]
            
            if (x_start, y_start) in visited:
                continue
                
            queue = deque([(x_start, y_start)])
            visited.add((x_start, y_start))
            area = 0
            
            while queue:
                x, y = queue.popleft()
                area += (min(x_end, x_lines[x_lines.index(x) + 1]) - x) * (min(y_end, y_lines[y_lines.index(y) + 1]) - y)
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    
                    if (nx, ny) in visited:
                        continue
                    
                    if not (x_start <= nx < x_end and y_start <= ny < y_end):
                        continue
                    
                    can_move = True
                    
                    if dx == 1:
                        for seg in vertical_segments:
                            if seg[0] == x and seg[1] <= y < seg[2]:
                                can_move = False
                                break
                    elif dx == -1:
                        for seg in vertical_segments:
                            if seg[0] == x - 1 and seg[1] <= y < seg[2]:
                                can_move = False
                                break
                    elif dy == 1:
                        for seg in horizontal_segments:
                            if seg[0] == y and seg[1] <= x < seg[2]:
                                can_move = False
                                break
                    elif dy == -1:
                        for seg in horizontal_segments:
                            if seg[0] == y - 1 and seg[1] <= x < seg[2]:
                                can_move = False
                                break
                    
                    if can_move:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            
            if area > 0:
                areas.append(area)
    
    areas.sort(reverse=True)
    for area in areas:
        print(area)

if __name__ == "__main__":
    main()
