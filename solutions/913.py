
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
        l = float(data[index+1])
        h = float(data[index+2])
        index += 3
        segments.append((d, l, h))
    
    low = 0.0
    high = float(M)
    best_speed = 0.0
    
    for _ in range(100):
        mid = (low + high) / 2.0
        total_time_without_fine = 0.0
        valid = True
        
        for d, l, h in segments:
            if mid > l:
                total_time_without_fine += d / mid + h
            else:
                total_time_without_fine += d / mid
        
        mid_next = (mid + high) / 2.0
        total_time_next = 0.0
        for d, l, h in segments:
            if mid_next > l:
                total_time_next += d / mid_next + h
            else:
                total_time_next += d / mid_next
        
        if total_time_next < total_time_without_fine:
            low = mid
            best_speed = mid_next
        else:
            high = mid
            best_speed = mid
    
    best_speed = round(best_speed)
    if best_speed > M:
        best_speed = M
    
    print(int(best_speed))

if __name__ == "__main__":
    main()
