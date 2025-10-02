
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO SOLUTION")
        return
        
    N = int(data[0])
    K = int(data[1])
    
    # Количество сегментов для каждой цифры
    seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    # DP для минимального числа
    min_dp = [[float('inf')] * (K + 1) for _ in range(N + 1)]
    min_dp[0][0] = 0
    
    for i in range(N):
        for j in range(K + 1):
            if min_dp[i][j] != float('inf'):
                start_digit = 0 if i > 0 else 1
                for d in range(start_digit, 10):
                    cost = seg[d]
                    if j + cost <= K:
                        if min_dp[i + 1][j + cost] > min_dp[i][j] * 10 + d:
                            min_dp[i + 1][j + cost] = min_dp[i][j] * 10 + d
    
    # DP для максимального числа
    max_dp = [[-1] * (K + 1) for _ in range(N + 1)]
    max_dp[0][0] = 0
    
    for i in range(N):
        for j in range(K + 1):
            if max_dp[i][j] != -1:
                start_digit = 0 if i > 0 else 1
                for d in range(start_digit, 10):
                    cost = seg[d]
                    if j + cost <= K:
                        if max_dp[i + 1][j + cost] < max_dp[i][j] * 10 + d:
                            max_dp[i + 1][j + cost] = max_dp[i][j] * 10 + d
    
    if min_dp[N][K] == float('inf') or max_dp[N][K] == -1:
        print("NO SOLUTION")
    else:
        print(str(min_dp[N][K]).zfill(N))
        print(str(max_dp[N][K]).zfill(N))

if __name__ == "__main__":
    main()
