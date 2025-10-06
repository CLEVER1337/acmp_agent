
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    times = []
    for i in range(1, n + 1):
        parts = data[i].split(':')
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        total_seconds = h * 3600 + m * 60 + s
        times.append(total_seconds)
    
    times.sort()
    max_interval = 0
    best_time = 0
    total_cycle = 12 * 3600
    
    for i in range(n):
        current = times[i]
        next_time = times[(i + 1) % n]
        if i == n - 1:
            interval = (total_cycle - current) + next_time
        else:
            interval = next_time - current
        
        if interval > max_interval:
            max_interval = interval
            best_time = (current + interval // 2) % total_cycle
    
    h = best_time // 3600
    best_time %= 3600
    m = best_time // 60
    s = best_time % 60
    print(f"{h}:{m:02d}:{s:02d}")

if __name__ == "__main__":
    main()
