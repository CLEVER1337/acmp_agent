
import sys

def main():
    data = sys.stdin.readline().split()
    N = int(data[0])
    K1 = int(data[1])
    K2 = int(data[2])
    S = int(data[3])
    
    dp = [[0.0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(N):
        dp[N][i] = 1.0
        dp[i][N] = 0.0
    
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            dp[i][j] = 0.5 * dp[i + 1][j] + 0.5 * dp[i][j + 1]
    
    p = dp[K1][K2]
    petya_coins = round(p * S)
    vasya_coins = S - petya_coins
    
    print(f"{petya_coins} {vasya_coins}")

if __name__ == "__main__":
    main()
