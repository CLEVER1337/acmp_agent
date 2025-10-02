
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    segments = []
    index = 2
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
    
    events.sort()
    
    queries = [(points[i], i) for i in range(m)]
    queries.sort()
    
    result = [0] * m
    count = 0
    event_idx = 0
    
    for point, idx in queries:
        while event_idx < len(events) and events[event_idx][0] <= point:
            count += events[event_idx][1]
            event_idx += 1
        result[idx] = count
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
