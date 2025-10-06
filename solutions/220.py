
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    U = int(data[idx]); idx += 1
    H = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    L = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    X = list(map(int, data[idx:idx+N]))
    
    if L < U:
        print(0)
        return
        
    lines = []
    for i in range(N):
        lines.append(X[i])
    
    total_scroll_steps = (L - U + T - 1) // T
    if total_scroll_steps < 0:
        total_scroll_steps = 0
    
    events = []
    for x in lines:
        start_pos = x
        end_pos = x - U + 1
        if end_pos > total_scroll_steps * T:
            continue
        if start_pos < 0:
            start_pos = 0
        first_step = (start_pos + T - 1) // T
        last_step = end_pos // T
        if last_step < 0:
            last_step = -1
        if first_step <= last_step:
            events.append((first_step, 1))
            events.append((last_step + 1, -1))
    
    events.sort(key=lambda x: (x[0], x[1]))
    
    min_crossings = float('inf')
    current = 0
    event_index = 0
    total_events = len(events)
    
    for step in range(total_scroll_steps + 1):
        while event_index < total_events and events[event_index][0] == step:
            current += events[event_index][1]
            event_index += 1
        if current < min_crossings:
            min_crossings = current
            
    if min_crossings == float('inf'):
        min_crossings = 0
        
    print(min_crossings)

if __name__ == "__main__":
    main()
