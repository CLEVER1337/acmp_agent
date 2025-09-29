
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    weights = list(map(int, data[1:1+n]))
    
    total = sum(weights)
    half = total // 2
    
    dp = [False] * (half + 1)
    dp[0] = True
    
    for w in weights:
        for j in range(half, w - 1, -1):
            if dp[j - w]:
                dp[j] = True
    
    max_sum = 0
    for j in range(half, -1, -1):
        if dp[j]:
            max_sum = j
            break
            
    result = total - 2 * max_sum
    print(result)

if __name__ == "__main__":
    main()
