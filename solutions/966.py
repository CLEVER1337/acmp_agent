
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    events = []
    index = 1
    for _ in range(n):
        l = int(data[index])
        r = int(data[index+1])
        v = int(data[index+2])
        index += 3
        events.append((l, v))
        events.append((r, -v))
    T = int(data[index])
    
    events.sort()
    current_volume = 0
    current_rate = 0
    prev_time = 0
    
    for time, dv in events:
        if time > T:
            break
            
        dt = time - prev_time
        current_volume += current_rate * dt
        prev_time = time
        current_rate += dv
        
        if current_volume < 0:
            current_volume = 0
    
    if prev_time < T:
        dt = T - prev_time
        current_volume += current_rate * dt
        if current_volume < 0:
            current_volume = 0
    
    print(current_volume)

if __name__ == "__main__":
    main()
