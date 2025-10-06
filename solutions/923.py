
def count_groups(n):
    if n < 3:
        return 0
    if n == 3:
        return 1
    
    memo = {}
    
    def dp(x):
        if x < 3:
            return 0
        if x == 3:
            return 1
        if x in memo:
            return memo[x]
        
        even = (x + 1) // 2
        odd = x // 2
        result = dp(even) + dp(odd)
        memo[x] = result
        return result
    
    return dp(n)

def main():
    n = int(input().strip())
    print(count_groups(n))

if __name__ == '__main__':
    main()
