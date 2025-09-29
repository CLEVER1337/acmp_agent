
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    W = int(data[0]); H = int(data[1])
    n = int(data[2])
    segments = []
    index = 3
    for i in range(n):
        a, b, c, d = map(int, data[index:index+4])
        index += 4
        if a == c:
            segments.append(('v', a, min(b, d), max(b, d)))
        elif b == d:
            segments.append(('h', b, min(a, c), max(a, c)))
    
    vertical_segments = [seg for seg in segments if seg[0] == 'v']
    horizontal_segments = [seg for seg in segments if seg[0] == 'h']
    
    vertical_segments.sort(key=lambda x: x[1])
    horizontal_segments.sort(key=lambda x: x[1])
    
    x_lines = [0, W]
    for seg in vertical_segments:
        x_lines.append(seg[1])
    x_lines = sorted(set(x_lines))
    
    y_lines = [0, H]
    for seg in horizontal_segments:
        y_lines.append(seg[1])
    y_lines = sorted(set(y_lines))
    
    areas = []
    for i in range(len(x_lines) - 1):
        x1 = x_lines[i]
        x2 = x_lines[i + 1]
        for j in range(len(y_lines) - 1):
            y1 = y_lines[j]
            y2 = y_lines[j + 1]
            
            cell_has_segment = False
            for seg in vertical_segments:
                if seg[1] == x1 and seg[2] <= y1 and seg[3] >= y2:
                    cell_has_segment = True
                    break
            for seg in horizontal_segments:
                if seg[1] == y1 and seg[2] <= x1 and seg[3] >= x2:
                    cell_has_segment = True
                    break
            
            if not cell_has_segment:
                area = (x2 - x1) * (y2 - y1)
                areas.append(area)
    
    areas.sort(reverse=True)
    for area in areas:
        print(area, end=' ')
    print()

if __name__ == "__main__":
    main()
