
def main():
    import sys
    data = sys.stdin.read().split()
    M = int(data[0])
    N = int(data[1])
    total = M * N
    
    if total == 0:
        print(0)
        return
        
    if M > N:
        M, N = N, M
        
    patterns = []
    
    def generate_patterns(pattern, pos):
        if pos == M:
            patterns.append(pattern)
            return
        generate_patterns(pattern, pos + 1)
        generate_patterns(pattern | (1 << pos), pos + 1)
    
    generate_patterns(0, 0)
    
    dp = {}
    for p in patterns:
        dp[p] = 1
        
    for i in range(1, N):
        new_dp = {}
        for prev in patterns:
            count = dp.get(prev, 0)
            if count == 0:
                continue
            for curr in patterns:
                valid = True
                for j in range(M - 1):
                    mask = (1 << j) | (1 << (j + 1))
                    if (prev & mask) == mask and (curr & mask) == mask:
                        valid = False
                        break
                    if (prev & mask) == 0 and (curr & mask) == 0:
                        valid = False
                        break
                if valid:
                    new_dp[curr] = new_dp.get(curr, 0) + count
        dp = new_dp
        
    result = sum(dp.values())
    print(result)

if __name__ == "__main__":
    main()
