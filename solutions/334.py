
def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_time(total_seconds):
    total_seconds %= 43200
    h = total_seconds // 3600
    if h == 0:
        h = 12
    total_seconds %= 3600
    m = total_seconds // 60
    s = total_seconds %= 60
    return f"{h}:{m:02d}:{s:02d}"

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
        total_seconds = time_to_seconds(h, m, s)
        times.append(total_seconds)
    
    times.sort()
    half_circle = 21600
    min_total = float('inf')
    best_time = 0
    
    for i in range(n):
        end = (i + n // 2) % n
        if i <= end:
            max_diff = times[end] - times[i]
        else:
            max_diff = 43200 - times[i] + times[end]
        
        if max_diff <= half_circle:
            total = max_diff
        else:
            total = 43200 - max_diff
        
        if total < min_total:
            min_total = total
            best_time = times[(i + n // 2) % n]
        elif total == min_total:
            candidate = times[(i + n // 2) % n]
            if candidate < best_time:
                best_time = candidate
    
    print(seconds_to_time(best_time))

if __name__ == "__main__":
    main()
