
def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_time(total_seconds):
    total_seconds %= 43200
    h = total_seconds // 3600
    if h == 0:
        h = 12
    total_seconds %= 3600
    m = total_seconds // 60
    s = total_seconds % 60
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
        times.append(time_to_seconds(h, m, s))
    
    times.sort()
    MOD = 43200
    
    def calculate_cost(target):
        total = 0
        for t in times:
            if t >= target:
                diff = t - target
            else:
                diff = MOD - target + t
            total += diff
        return total
    
    min_cost = float('inf')
    best_time = 0
    
    for t in times:
        cost = calculate_cost(t)
        if cost < min_cost:
            min_cost = cost
            best_time = t
    
    print(seconds_to_time(best_time))

if __name__ == "__main__":
    main()
