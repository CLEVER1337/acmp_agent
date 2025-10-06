
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    S = list(map(int, data[1:1+n]))
    k = int(data[1+n])
    V = list(map(int, data[2+n:2+n+k]))
    
    left = 0.0
    right = 1e9
    for _ in range(100):
        mid = (left + right) / 2.0
        total = 0.0
        for v in V:
            total += v * mid
        required = sum(S)
        if total >= required:
            right = mid
        else:
            left = mid
            
    T = (left + right) / 2.0
    
    print("{:.6f}".format(T))
    
    firms = sorted([(v, idx) for idx, v in enumerate(V)], reverse=True)
    objects = sorted([(s, idx) for idx, s in enumerate(S)], reverse=True)
    
    assignments = []
    current_time = 0.0
    firm_idx = 0
    
    for s, obj_idx in objects:
        while s > 0:
            v, firm_j = firms[firm_idx]
            work_time = min(s / v, T - current_time)
            if work_time > 1e-9:
                assignments.append((current_time, obj_idx + 1, firm_j + 1))
                s -= v * work_time
                current_time += work_time
            if s > 1e-9:
                firm_idx += 1
                current_time = 0.0
    
    assignments.sort(key=lambda x: x[0])
    
    for t, i, j in assignments:
        print("{:.6f} {} {}".format(t, i, j))

if __name__ == "__main__":
    main()
