
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    events = []
    for i in range(1, n):
        parts = data[i].split()
        f = float(parts[0])
        word = parts[1]
        events.append((f, word))
    
    low = 30.0
    high = 4000.0
    prev_f = float(data[1].split()[0])
    
    for i in range(len(events)):
        current_f, word = events[i]
        if current_f == prev_f:
            continue
            
        mid = (prev_f + current_f) / 2.0
        
        if word == 'closer':
            if current_f > prev_f:
                high = min(high, mid)
            else:
                low = max(low, mid)
        else:  # further
            if current_f > prev_f:
                low = max(low, mid)
            else:
                high = min(high, mid)
                
        prev_f = current_f
    
    print(f"{low:.6f} {high:.6f}")

if __name__ == "__main__":
    main()
