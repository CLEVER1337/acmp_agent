
def main():
    n = int(input().strip())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - j][j] + dp[i][j - 1]
        for j in range(i + 1, n + 1):
            dp[i][j] = dp[i][i]
            
    max_val = -1
    best_partition = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] > max_val:
                max_val = dp[i][j]
                
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j] == max_val:
                temp_i, temp_j = i, j
                partition = []
                while temp_i > 0:
                    if temp_j <= temp_i:
                        partition.append(temp_j)
                        temp_i -= temp_j
                    else:
                        temp_j = temp_i
                best_partition = partition
                break
        if best_partition:
            break
            
    print(max_val)
    print(' '.join(map(str, best_partition)))

if __name__ == '__main__':
    main()
