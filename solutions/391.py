
def main():
    import sys
    data = sys.stdin.read().split()
    x = int(data[0])
    m = int(data[1])
    L = int(data[2])
    v = int(data[3])
    
    max_digit = 9
    n = L
    
    dp = [[-1] * m for _ in range(n+1)]
    dp[0][0] = 0
    
    for i in range(n):
        for rem in range(m):
            if dp[i][rem] != -1:
                for d in range(max_digit + 1):
                    new_rem = (rem * x + d) % m
                    if dp[i+1][new_rem] == -1:
                        dp[i+1][new_rem] = d
    
    if dp[n][v] == -1:
        print("NO SOLUTION")
        return
        
    s = []
    current_rem = v
    for i in range(n, 0, -1):
        d = dp[i][current_rem]
        s.append(str(d))
        prev_rem = (current_rem - d) % m
        prev_rem = (prev_rem * pow(x, -1, m)) % m
        current_rem = prev_rem
        
    result = ''.join(reversed(s))
    print(result)

if __name__ == "__main__":
    main()
