
segments = {
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
    '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO SOLUTION")
        return
        
    N = int(data[0])
    K = int(data[1])
    
    min_dp = [None] * (K + 1)
    max_dp = [None] * (K + 1)
    
    min_dp[0] = ""
    max_dp[0] = ""
    
    for i in range(N):
        new_min = [None] * (K + 1)
        new_max = [None] * (K + 1)
        
        for s in range(K + 1):
            if min_dp[s] is None:
                continue
                
            for digit in range(10):
                if i == 0 and digit == 0:
                    continue
                    
                seg = segments[str(digit)]
                new_s = s + seg
                if new_s > K:
                    continue
                    
                candidate_min = min_dp[s] + str(digit)
                candidate_max = max_dp[s] + str(digit)
                
                if new_min[new_s] is None or candidate_min < new_min[new_s]:
                    new_min[new_s] = candidate_min
                    
                if new_max[new_s] is None or candidate_max > new_max[new_s]:
                    new_max[new_s] = candidate_max
                    
        min_dp = new_min
        max_dp = new_max
        
    if min_dp[K] is None or max_dp[K] is None:
        print("NO SOLUTION")
    else:
        print(min_dp[K])
        print(max_dp[K])

if __name__ == "__main__":
    main()
