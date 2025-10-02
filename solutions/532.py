
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
    
    events = []
    total = 0
    
    for i in range(n):
        idx = 3 + i * 4
        a = int(data[idx])
        b = int(data[idx + 1])
        c = int(data[idx + 2])
        d = int(data[idx + 3])
        
        total += b * (d - c)
        diff = a - b
        events.append((c, diff, 1))
        events.append((d, -diff, 0))
    
    events.sort()
    
    diffs = []
    current_diff = 0
    prev_stop = 1
    
    for stop, diff, typ in events:
        if stop > prev_stop:
            diffs.append(current_diff)
            prev_stop = stop
        
        current_diff += diff
    
    diffs.sort(reverse=True)
    
    for i in range(min(m, len(diffs))):
        if diffs[i] > 0:
            total += diffs[i]
    
    print(total)

if __name__ == "__main__":
    main()
