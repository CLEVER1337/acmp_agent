
def read_rects():
    k = int(input())
    rects = []
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        rects.append((x1, y1, x2, y2))
    return rects

def get_events(rects):
    events = []
    for x1, y1, x2, y2 in rects:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
    events.sort()
    return events

def add_segment(segments, y1, y2):
    new_segments = []
    for seg in segments:
        s1, s2 = seg
        if s2 <= y1 or s1 >= y2:
            new_segments.append(seg)
        else:
            if s1 < y1:
                new_segments.append((s1, y1))
            if s2 > y2:
                new_segments.append((y2, s2))
    segments[:] = new_segments

def remove_segment(segments, y1, y2):
    new_segments = []
    i = 0
    n = len(segments)
    while i < n:
        s1, s2 = segments[i]
        if s2 <= y1 or s1 >= y2:
            new_segments.append(segments[i])
            i += 1
        else:
            if s1 < y1:
                new_segments.append((s1, y1))
            if s2 > y2:
                new_segments.append((y2, s2))
            i += 1
    segments[:] = new_segments

def count_holes(events):
    segments = []
    count = 0
    prev_x = -1
    for event in events:
        x, op, y1, y2 = event
        if segments and x > prev_x:
            count += len(segments) * (x - prev_x)
        if op == 1:
            add_segment(segments, y1, y2)
        else:
            remove_segment(segments, y1, y2)
        prev_x = x
    return count

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    idx = 0
    N = int(data[idx]); M = int(data[idx+1]); idx += 2
    K1 = int(data[idx]); idx += 1
    rects1 = []
    for i in range(K1):
        x1 = int(data[idx]); y1 = int(data[idx+1]); x2 = int(data[idx+2]); y2 = int(data[idx+3]); idx += 4
        rects1.append((x1, y1, x2, y2))
        
    K2 = int(data[idx]); idx += 1
    rects2 = []
    for i in range(K2):
        x1 = int(data[idx]); y1 = int(data[idx+1]); x2 = int(data[idx+2]); y2 = int(data[idx+3]); idx += 4
        rects2.append((x1, y1, x2, y2))
    
    events1 = get_events(rects1)
    events2 = get_events(rects2)
    
    total1 = count_holes(events1)
    total2 = count_holes(events2)
    
    combined_rects = rects1 + rects2
    events_combined = get_events(combined_rects)
    total_combined = count_holes(events_combined)
    
    result = total1 + total2 - total_combined
    print(result)

if __name__ == "__main__":
    main()
