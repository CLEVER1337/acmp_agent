
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("No solution.")
        return
        
    try:
        N = int(data[0])
        w = int(data[1])
        L = int(data[2])
        r = int(data[3])
        R = int(data[4])
        costs = list(map(int, data[5:5+L]))
    except:
        print("No solution.")
        return
        
    if N == 0:
        print(0)
        return
        
    if L < w:
        print("No solution.")
        return
        
    min_distance = r
    max_distance = R
    
    total_length_needed = (N - 1) * min_distance + w
    if total_length_needed > L:
        print("No solution.")
        return
        
    dp = [float('inf')] * (L + 1)
    prefix_sum = [0] * (L + 1)
    
    for i in range(1, L + 1):
        prefix_sum[i] = prefix_sum[i - 1] + costs[i - 1]
        
    def get_sum(l, r):
        if l < 1:
            l = 1
        if r > L:
            r = L
        return prefix_sum[r] - prefix_sum[l - 1]
        
    for pos in range(1, L - w + 2):
        dp[pos] = get_sum(pos, pos + w - 1)
        
    for stop in range(2, N + 1):
        new_dp = [float('inf')] * (L + 1)
        
        for prev_pos in range(1, L + 1):
            if dp[prev_pos] == float('inf'):
                continue
                
            min_next = prev_pos + w + min_distance
            max_next = prev_pos + w + max_distance
            
            if min_next > L:
                continue
                
            start = min_next
            end = min(max_next, L - w + 1)
            
            for next_pos in range(start, end + 1):
                cost = dp[prev_pos] + get_sum(next_pos, next_pos + w - 1)
                if cost < new_dp[next_pos]:
                    new_dp[next_pos] = cost
                    
        dp = new_dp
        
    result = min(dp)
    if result == float('inf'):
        print("No solution.")
    else:
        print(result)

if __name__ == "__main__":
    main()
