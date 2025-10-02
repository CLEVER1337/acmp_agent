
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cycles = []
    index = 1
    for i in range(n):
        L = int(data[index])
        R = int(data[index + 1])
        index += 2
        cycles.append((L, R))
    
    dp = [0] * (n + 1)
    dp[n] = 1
    
    for i in range(n - 1, -1, -1):
        L, R = cycles[i]
        if L < 0:
            var_index = -L - 1
            if var_index >= i:
                dp[i] = dp[i + 1] * max(0, R - dp[var_index] + 1)
            else:
                dp[i] = dp[i + 1] * max(0, R - dp[var_index] + 1)
        else:
            dp[i] = dp[i + 1] * max(0, R - L + 1)
    
    print(dp[0])

if __name__ == "__main__":
    main()
