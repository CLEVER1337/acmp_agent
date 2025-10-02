
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
        D = float(data[index])
        L = float(data[index+1])
        H = float(data[index+2])
        index += 3
        segments.append((D, L, H))
    
    left = 0.0
    right = float(M)
    best_speed = 0.0
    
    for _ in range(100):
        mid = (left + right) / 2.0
        total_time = 0.0
        valid = True
        
        for D, L, H in segments:
            if mid > L:
                total_time += H
            total_time += D / mid
            
        mid_next = (mid + right) / 2.0
        total_time_next = 0.0
        for D, L, H in segments:
            if mid_next > L:
                total_time_next += H
            total_time_next += D / mid_next
            
        if total_time_next < total_time:
            left = mid
        else:
            right = mid
            
    best_speed = left
    
    print(int(best_speed + 0.5))

if __name__ == "__main__":
    main()
