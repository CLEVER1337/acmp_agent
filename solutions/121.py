
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        coords = list(map(int, f.readline().split()))
    
    coords.sort()
    dp = [0] * n
    dp[1] = coords[1] - coords[0]
    
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + (coords[i] - coords[i-1])
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n-1]))

if __name__ == "__main__":
    main()
