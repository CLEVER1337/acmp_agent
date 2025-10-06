
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
    for i in range(n - 1, -1, -1):
        L, R = cycles[i]
        if L < 0:
            var_index = -L - 1
            if var_index >= i:
                dp[i] = 0
            else:
                left_val = dp[var_index]
        else:
            left_val = L
        
        if left_val > R:
            dp[i] = 0
        else:
            if i == n - 1:
                dp[i] = R - left_val + 1
            else:
                total = 0
                for j in range(left_val, R + 1):
                    total += dp[i + 1]
                dp[i] = total
    
    result = dp[0] if n > 0 else 0
    print(result)

if __name__ == "__main__":
    main()
