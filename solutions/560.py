
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("No solution.")
        return
        
    try:
        N = int(data[0]); w = int(data[1]); L = int(data[2])
        r = int(data[3]); R = int(data[4])
        costs = list(map(int, data[5:5+L]))
    except:
        print("No solution.")
        return
        
    if L < w:
        print("No solution.")
        return
        
    min_cost = float('inf')
    
    dp = [[float('inf')] * L for _ in range(N)]
    
    for pos in range(L - w + 1):
        total_cost = sum(costs[pos:pos+w])
        dp[0][pos] = total_cost
        
    for i in range(1, N):
        for j in range(L - w + 1):
            if dp[i-1][j] == float('inf'):
                continue
                
            current_end = j + w - 1
            next_start_min = current_end + r + 1
            next_start_max = current_end + R + 1
            
            for k in range(max(0, next_start_min), min(L - w + 1, next_start_max + 1)):
                if k >= L:
                    continue
                total_cost = sum(costs[k:k+w])
                if dp[i][k] > dp[i-1][j] + total_cost:
                    dp[i][k] = dp[i-1][j] + total_cost
                    
    for pos in range(L - w + 1):
        if dp[N-1][pos] < min_cost:
            min_cost = dp[N-1][pos]
            
    if min_cost == float('inf'):
        print("No solution.")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
