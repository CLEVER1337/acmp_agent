
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    idx = 0
    M = int(data[idx]); idx += 1
    trees = []
    for i in range(M):
        W = int(data[idx]); E = int(data[idx+1]); idx += 2
        trees.append((W, E))
        
    N = int(data[idx]); idx += 1
    flowerbeds = []
    for i in range(N):
        flowerbeds.append(int(data[idx])); idx += 1
        
    dp = [0] * (N + 1)
    
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i])
        for w, e in trees:
            left_bound = flowerbeds[i] - w
            right_bound = flowerbeds[i] + e
            
            j = i + 1
            while j < N and flowerbeds[j] < right_bound:
                j += 1
                
            dp[j] = max(dp[j], dp[i] + 1)
            
    print(dp[N])

if __name__ == "__main__":
    main()
