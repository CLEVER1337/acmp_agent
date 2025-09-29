
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    rects = []
    index = 1
    for i in range(n):
        x1 = int(data[index]); y1 = int(data[index+1])
        x2 = int(data[index+2]); y2 = int(data[index+3])
        index += 4
        rects.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    
    events = []
    for x1, y1, x2, y2 in rects:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
    events.sort()
    
    active = []
    total_area = 0
    prev_x = events[0][0]
    
    for event in events:
        x, typ, y1, y2 = event
        if x != prev_x:
            width = x - prev_x
            height = 0
            current_start = -10**9
            current_end = -10**9
            
            for seg in sorted(active):
                if seg[0] > current_end:
                    height += current_end - current_start
                    current_start, current_end = seg
                else:
                    current_end = max(current_end, seg[1])
            
            height += current_end - current_start
            total_area += width * height
            prev_x = x
        
        if typ == 1:
            active.append((y1, y2))
        else:
            active.remove((y1, y2))
    
    print(total_area)

if __name__ == "__main__":
    main()
