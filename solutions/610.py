
def main():
    with open('INPUT.TXT', 'r') as f:
        r, c = map(int, f.readline().split())
    
    n = r * c
    
    if n % 2 != 0:
        print(0)
        return
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i - 2] * 3
        else:
            dp[i] = dp[i - 1]
    
    result = dp[n]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
