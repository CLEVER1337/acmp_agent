
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
    for x1, y1, x2, y2 in rects:
        events.append((x1, y1, y2, 1))
        events.append((x2, y1, y2, -1))
    events.sort()
    return events

def process_events(events):
    active = []
    result = []
    prev_x = None
    
    for x, y1, y2, event_type in events:
        if prev_x is not None and x != prev_x:
            if active:
                active.sort()
                merged = []
                start, end = active[0]
                for i in range(1, len(active)):
                    if active[i][0] <= end:
                        end = max(end, active[i][1])
                    else:
                        merged.append((start, end))
                        start, end = active[i]
                merged.append((start, end))
                result.append((prev_x, x, merged))
        
        if event_type == 1:
            active.append((y1, y2))
        else:
            new_active = []
            for seg in active:
                if seg != (y1, y2):
                    new_active.append(seg)
            active = new_active
        
        prev_x = x
    
    return result

def count_holes(intervals1, intervals2):
    total = 0
    for x1_start, x1_end, y_segments1 in intervals1:
        for x2_start, x2_end, y_segments2 in intervals2:
            x_overlap_start = max(x1_start, x2_start)
            x_overlap_end = min(x1_end, x2_end)
            
            if x_overlap_start < x_overlap_end:
                for seg1 in y_segments1:
                    for seg2 in y_segments2:
                        y_overlap_start = max(seg1[0], seg2[0])
                        y_overlap_end = min(seg1[1], seg2[1])
                        if y_overlap_start < y_overlap_end:
                            total += 1
    return total

def main():
    rects1 = read_rects()
    rects2 = read_rects()
    
    events1 = get_events(rects1)
    events2 = get_events(rects2)
    
    intervals1 = process_events(events1)
    intervals2 = process_events(events2)
    
    result = count_holes(intervals1, intervals2)
    print(result)

if __name__ == "__main__":
    main()
