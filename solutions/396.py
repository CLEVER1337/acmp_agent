
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    index = 2
    
    segments = []
    for i in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        segments.append((min(a, b), max(a, b)))
    
    points = list(map(int, data[index:index + m]))
    
    events = []
    for seg in segments:
        events.append((seg[0], 1))
        events.append((seg[1] + 1, -1))
    
    events.sort(key=lambda x: x[0])
    
    point_events = [(points[i], i) for i in range(m)]
    point_events.sort(key=lambda x: x[0])
    
    result = [0] * m
    current_count = 0
    event_index = 0
    events_len = len(events)
    
    for point, orig_index in point_events:
        while event_index < events_len and events[event_index][0] <= point:
            current_count += events[event_index][1]
            event_index += 1
        result[orig_index] = current_count
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
