
def read_rects():
    n, m = map(int, input().split())
    k = int(input())
    rects = []
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        rects.append((x1, y1, x2, y2))
    return rects

def get_events(rects):
    events = []
    for i, (x1, y1, x2, y2) in enumerate(rects):
        events.append((x1, 1, i))
        events.append((x2, -1, i))
    events.sort()
    return events

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n1, m1 = int(data[idx]), int(data[idx+1]); idx += 2
    k1 = int(data[idx]); idx += 1
    rects1 = []
    for _ in range(k1):
        x1, y1, x2, y2 = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        rects1.append((x1, y1, x2, y2))
        
    n2, m2 = int(data[idx]), int(data[idx+1]); idx += 2
    k2 = int(data[idx]); idx += 1
    rects2 = []
    for _ in range(k2):
        x1, y1, x2, y2 = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        rects2.append((x1, y1, x2, y2))
    
    events1 = get_events(rects1)
    events2 = get_events(rects2)
    
    active1 = set()
    active2 = set()
    
    i1 = i2 = 0
    result = 0
    
    while i1 < len(events1) and i2 < len(events2):
        if events1[i1][0] <= events2[i2][0]:
            x, op, idx = events1[i1]
            if op == 1:
                active1.add(idx)
            else:
                active1.discard(idx)
            i1 += 1
        else:
            x, op, idx = events2[i2]
            if op == 1:
                active2.add(idx)
            else:
                active2.discard(idx)
            i2 += 1
        
        if active1 and active2:
            result = max(result, len(active1) + len(active2))
    
    print(result)

if __name__ == "__main__":
    main()
