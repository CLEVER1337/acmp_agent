
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    s = int(data[1])
    nums = list(map(int, data[2:2+n]))
    
    total_sum = sum(nums)
    if (total_sum + s) % 2 != 0:
        print("No solution")
        return
        
    target = (total_sum + s) // 2
    if target < 0 or target > total_sum:
        print("No solution")
        return
        
    dp = [0] * (target + 1)
    dp[0] = 1
    path = [set() for _ in range(target + 1)]
    path[0].add(0)
    
    for i in range(n):
        num = nums[i]
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] += dp[j - num]
                for p in path[j - num]:
                    path[j].add(p | (1 << i))
                    
    if not dp[target]:
        print("No solution")
        return
        
    signs = ['+'] * n
    solution_mask = next(iter(path[target]))
    
    for i in range(n):
        if solution_mask & (1 << i):
            signs[i] = '+'
        else:
            signs[i] = '-'
            
    result = str(nums[0])
    for i in range(1, n):
        result += signs[i] + str(nums[i])
        
    result += '=' + str(s)
    print(result)

if __name__ == "__main__":
    main()
