
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:1+n]))
    
    if n == 1:
        print(0)
        return
        
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    
    for i in range(2, n):
        option1 = dp[i-1] + abs(heights[i] - heights[i-1])
        option2 = dp[i-2] + 3 * abs(heights[i] - heights[i-2])
        dp[i] = min(option1, option2)
        
    print(dp[n-1])

if __name__ == "__main__":
    main()
