
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("No solution")
        return
        
    n = int(data[0])
    s = int(data[1])
    numbers = list(map(int, data[2:2+n]))
    
    total_sum = sum(numbers)
    if (total_sum - s) % 2 != 0 or abs(s) > total_sum:
        print("No solution")
        return
        
    target = (total_sum - s) // 2
    if target < 0:
        print("No solution")
        return
        
    dp = [False] * (target + 1)
    dp[0] = True
    parent = [-1] * (target + 1)
    
    for i in range(n):
        num = numbers[i]
        for j in range(target, num - 1, -1):
            if dp[j - num] and not dp[j]:
                dp[j] = True
                parent[j] = i
    
    if not dp[target]:
        print("No solution")
        return
        
    signs = ['+'] * n
    current = target
    while current > 0:
        idx = parent[current]
        signs[idx] = '-'
        current -= numbers[idx]
    
    result = str(numbers[0])
    for i in range(1, n):
        result += signs[i] + str(numbers[i])
        
    result += '=' + str(s)
    print(result)

if __name__ == "__main__":
    main()
