
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    M = int(data[1])
    segments = []
    index = 2
    for i in range(n):
        d = float(data[index])
        L = float(data[index+1])
        H = float(data[index+2])
        index += 3
        segments.append((d, L, H))
    
    def total_time(speed):
        if speed <= 0:
            return float('inf')
        total = 0.0
        for d, L, H in segments:
            if speed > L:
                total += H
            total += d / speed
        return total
    
    left = 0.0
    right = M
    best_speed = M
    eps = 1e-9
    
    for _ in range(100):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        t1 = total_time(mid1)
        t2 = total_time(mid2)
        if t1 < t2:
            right = mid2
        else:
            left = mid1
    
    best_speed = (left + right) / 2
    best_time = total_time(best_speed)
    
    candidate_speeds = [M]
    for d, L, H in segments:
        candidate_speeds.append(L)
    
    candidate_speeds.sort()
    for speed in candidate_speeds:
        if speed <= M:
            t = total_time(speed)
            if t < best_time - eps:
                best_time = t
                best_speed = speed
            elif abs(t - best_time) < eps and speed > best_speed:
                best_speed = speed
    
    print(int(best_speed + 0.5))

if __name__ == "__main__":
    main()
