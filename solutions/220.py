
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    U = int(data[idx]); idx += 1
    H = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    L = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    X = list(map(int, data[idx:idx+N]))
    
    if X[N-1] < U:
        print(0)
        return
        
    total_scroll_steps = (X[N-1] - U + T) // T
    if (X[N-1] - U) % T != 0:
        total_scroll_steps += 1
        
    events = []
    for line in X:
        events.append((line, 1))
        events.append((line + H, -1))
        
    events.sort()
    
    best_count = float('inf')
    for start_pos in range(0, U - H + 1):
        count = 0
        for event_pos, event_type in events:
            scroll_pos = event_pos - start_pos
            if scroll_pos < 0:
                continue
            if scroll_pos > total_scroll_steps * T:
                continue
                
            first_step = (scroll_pos + T - 1) // T
            if first_step < 0:
                first_step = 0
                
            if event_type == 1:
                count += first_step
            else:
                count -= first_step
                
        best_count = min(best_count, count)
        
    print(best_count)

if __name__ == "__main__":
    main()
