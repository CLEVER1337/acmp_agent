
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    
    max_sum = sum(A)
    dp = [False] * (max_sum + 1)
    dp[0] = True
    
    for num in A:
        for s in range(max_sum, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
                
    count = sum(dp)
    print(count)

if __name__ == "__main__":
    main()
