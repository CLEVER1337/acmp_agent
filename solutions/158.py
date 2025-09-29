
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        X = int(data[0])
        K = int(data[1])
    
    n = K + 1
    total_notes = X // 5
    
    dp = [[0] * (total_notes + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(total_notes + 1):
            dp[i][j] = sum(dp[i-1][k] for k in range(j + 1))
    
    print(dp[n][total_notes], file=open("OUTPUT.TXT", "w"))

if __name__ == "__main__":
    main()
