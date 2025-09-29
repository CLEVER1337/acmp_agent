
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    k = int(data[1])
    T = int(data[2])
    
    Ti = list(map(int, data[3:3+n]))
    Pi = list(map(int, data[3+n:3+2*n]))
    Si = list(map(int, data[3+2*n:3+3*n]))
    
    gangsters = sorted(zip(Ti, Pi, Si), key=lambda x: x[0])
    
    dp = [-10**9] * (k + 1)
    dp[0] = 0
    
    max_wealth = 0
    prev_time = 0
    
    for t, p, s in gangsters:
        if t > T:
            continue
            
        new_dp = [-10**9] * (k + 1)
        
        for door_state in range(k + 1):
            if dp[door_state] == -10**9:
                continue
                
            time_diff = t - prev_time
            min_possible = max(0, door_state - time_diff)
            max_possible = min(k, door_state + time_diff)
            
            for new_state in range(min_possible, max_possible + 1):
                if new_state == s:
                    new_dp[new_state] = max(new_dp[new_state], dp[door_state] + p)
                else:
                    new_dp[new_state] = max(new_dp[new_state], dp[door_state])
        
        dp = new_dp
        prev_time = t
        max_wealth = max(max_wealth, max(dp))
    
    print(max_wealth)

if __name__ == "__main__":
    main()
