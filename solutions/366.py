
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    s = int(data[1])
    nums = list(map(int, data[2:2+n]))
    
    total = sum(nums)
    if (total - s) % 2 != 0 or s > total or s < -total:
        print("No solution")
        return
        
    target = (total - s) // 2
    if target < 0:
        print("No solution")
        return
        
    dp = [False] * (target + 1)
    dp[0] = True
    prev = [None] * (target + 1)
    
    for i in range(n):
        num = nums[i]
        for j in range(target, num - 1, -1):
            if dp[j - num] and not dp[j]:
                dp[j] = True
                prev[j] = i
                
    if not dp[target]:
        print("No solution")
        return
        
    signs = ['+'] * n
    current = target
    while current > 0:
        idx = prev[current]
        signs[idx] = '-'
        current -= nums[idx]
        
    result = str(nums[0])
    for i in range(1, n):
        result += signs[i] + str(nums[i])
        
    print(result + '=' + str(s))

if __name__ == "__main__":
    main()
