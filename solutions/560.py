
import sys

def main():
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
        a_list = list(map(int, data[5:5+L]))
    except:
        print("No solution.")
        return
        
    if N == 0:
        print(0)
        return
        
    if w == 0:
        print(0)
        return
        
    total_length = L
    platform_length = w
    
    left_bound = 0
    right_bound = total_length - platform_length
    
    if right_bound < left_bound:
        print("No solution.")
        return
        
    min_gap = r
    max_gap = R
    
    dp = [float('inf')] * (right_bound + 1)
    cost_prefix = [0] * (total_length + 1)
    
    for i in range(1, total_length + 1):
        cost_prefix[i] = cost_prefix[i-1] + a_list[i-1]
        
    def get_cost(start, end):
        if start < 0:
            start = 0
        if end > total_length:
            end = total_length
        return cost_prefix[end] - cost_prefix[start]
        
    for pos in range(left_bound, right_bound + 1):
        dp[pos] = get_cost(pos, pos + platform_length)
        
    for stop in range(1, N):
        new_dp = [float('inf')] * (right_bound + 1)
        for prev_pos in range(left_bound, right_bound + 1):
            if dp[prev_pos] == float('inf'):
                continue
                
            min_next = prev_pos + platform_length + min_gap
            max_next = prev_pos + platform_length + max_gap
            
            min_next = max(min_next, left_bound)
            max_next = min(max_next, right_bound)
            
            if min_next > max_next:
                continue
                
            for next_pos in range(min_next, max_next + 1):
                cost = dp[prev_pos] + get_cost(next_pos, next_pos + platform_length)
                if cost < new_dp[next_pos]:
                    new_dp[next_pos] = cost
                    
        dp = new_dp
        
    result = min(dp) if min(dp) != float('inf') else float('inf')
    
    if result == float('inf'):
        print("No solution.")
    else:
        print(result)

if __name__ == "__main__":
    main()
