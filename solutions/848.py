
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    prev = [-1] * (n + 1)
    
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1]:
                if dp[i] + 1 < dp[j+1]:
                    dp[j+1] = dp[i] + 1
                    prev[j+1] = i
    
    result = []
    pos = n
    while pos > 0:
        start = prev[pos]
        result.append(s[start:pos])
        pos = start
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{dp[n]}\n")
        for pal in reversed(result):
            f.write(f"{pal}\n")

if __name__ == "__main__":
    main()
