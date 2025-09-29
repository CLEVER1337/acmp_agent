
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
    
    events = []
    base_sum = 0
    passengers = []
    
    index = 3
    for i in range(n):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        d = int(data[index+3])
        index += 4
        passengers.append((a, b, c, d))
        base_sum += b * (d - c)
        events.append((c, 1, a - b))
        events.append((d, -1, a - b))
    
    events.sort(key=lambda x: (x[0], x[1]))
    
    diffs = []
    current_diff = 0
    prev_stop = 1
    
    i = 0
    while i < len(events):
        current_stop = events[i][0]
        if current_stop > prev_stop:
            diffs.append((prev_stop, current_diff))
        
        while i < len(events) and events[i][0] == current_stop:
            if events[i][1] == 1:
                current_diff += events[i][2]
            else:
                current_diff -= events[i][2]
            i += 1
        
        prev_stop = current_stop
    
    diffs = [diff for _, diff in diffs]
    diffs.sort(reverse=True)
    
    additional_sum = 0
    for i in range(min(m, len(diffs))):
        if diffs[i] > 0:
            additional_sum += diffs[i]
    
    result = base_sum + additional_sum
    print(result)

if __name__ == "__main__":
    main()
