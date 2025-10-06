
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    M = int(data[idx]); idx += 1
    shadows = []
    for _ in range(M):
        w = int(data[idx]); e = int(data[idx+1]); idx += 2
        shadows.append((w, e))
    
    N = int(data[idx]); idx += 1
    beds = []
    for _ in range(N):
        beds.append(int(data[idx])); idx += 1
    
    dp = [0] * (N + 1)
    for i in range(N):
        max_prev = 0
        for j in range(i):
            if dp[j] > max_prev:
                max_prev = dp[j]
        dp[i] = max_prev + 1
        
        for w, e in shadows:
            left_bound = beds[i] - w
            right_bound = beds[i] + e
            
            k = i + 1
            while k < N and beds[k] < right_bound:
                if beds[k] > left_bound:
                    dp[k] = max(dp[k], max_prev + 1)
                k += 1
                
    result = max(dp) if N > 0 else 0
    print(result)

if __name__ == "__main__":
    main()
