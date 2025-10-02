
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    S = list(map(int, data[1:1+n]))
    k = int(data[1+n])
    V = list(map(int, data[2+n:2+n+k]))
    
    left = 0.0
    right = sum(S) / min(V) * 2
    
    for _ in range(100):
        mid = (left + right) / 2
        total_work = 0
        for v in V:
            total_work += v * mid
        
        if total_work >= sum(S):
            right = mid
        else:
            left = mid
    
    T = (left + right) / 2
    
    events = []
    remaining_S = S.copy()
    firm_available_time = [0.0] * k
    
    for obj_idx in range(n):
        min_start_time = float('inf')
        best_firm = -1
        
        for firm_idx in range(k):
            if firm_available_time[firm_idx] < min_start_time:
                min_start_time = firm_available_time[firm_idx]
                best_firm = firm_idx
        
        work_needed = remaining_S[obj_idx]
        work_time = work_needed / V[best_firm]
        
        events.append((min_start_time, obj_idx + 1, best_firm + 1))
        firm_available_time[best_firm] = min_start_time + work_time
        remaining_S[obj_idx] = 0
    
    print(f"{T:.6f}")
    for event in sorted(events, key=lambda x: x[0]):
        print(f"{event[0]:.6f} {event[1]} {event[2]}")

if __name__ == "__main__":
    main()
