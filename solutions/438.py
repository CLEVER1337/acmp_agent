
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
    right = sum(S) / min(V) + 1.0
    
    for _ in range(100):
        mid = (left + right) / 2.0
        total_work = 0.0
        for v in V:
            total_work += v * mid
        
        if total_work >= sum(S):
            right = mid
        else:
            left = mid
    
    T = (left + right) / 2.0
    
    print("{:.6f}".format(T))
    
    firm_capacity = [v * T for v in V]
    events = []
    current_firm_work = [0.0] * k
    
    for i in range(n):
        remaining = S[i]
        for j in range(k):
            if remaining <= 0:
                break
            if firm_capacity[j] - current_firm_work[j] > 1e-9:
                work_time = min(remaining, firm_capacity[j] - current_firm_work[j]) / V[j]
                start_time = current_firm_work[j] / V[j]
                events.append((start_time, i+1, j+1))
                current_firm_work[j] += min(remaining, firm_capacity[j] - current_firm_work[j])
                remaining -= min(remaining, firm_capacity[j] - current_firm_work[j])
    
    events.sort(key=lambda x: x[0])
    for event in events:
        print("{:.6f} {} {}".format(event[0], event[1], event[2]))

if __name__ == "__main__":
    main()
