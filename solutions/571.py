
def solve(n, sides):
    dp = [0] * (n + 1)
    dp[0] = 1  # базовый случай: пустой шоколад
    vertical_count = 0
    
    for i in range(1, n + 1):
        if sides[i - 1] == 'V':
            vertical_count += 1
            
        dp[i] = dp[i - 1] * 2 + (dp[vertical_count] if vertical_count > 0 else 0)
        
    return dp[-1] % (10**9 + 7) # возвращаем результат по модулю, чтобы избежать переполнения в случае больших чисел

if __name__ == '__main__':
    n = int(input())
    sides = input()
    
    print(solve(n, sides))
