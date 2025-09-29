
def main():
    import sys
    sys.setrecursionlimit(10000)
    
    n = int(sys.stdin.readline().strip())
    
    if n == 1:
        print(1)
        return
        
    dp = {}
    
    def dfs(count, product, sum_val, last):
        if count == n:
            return 1 if product == sum_val else 0
            
        key = (count, product, sum_val, last)
        if key in dp:
            return dp[key]
            
        res = 0
        start = last
        max_val = n + 1
        
        for num in range(start, max_val + 1):
            new_count = count + 1
            new_product = product * num
            new_sum = sum_val + num
            
            if new_product > new_sum + (n - new_count):
                break
                
            res += dfs(new_count, new_product, new_sum, num)
            
        dp[key] = res
        return res
        
    result = dfs(0, 1, 0, 2)
    print(result)

if __name__ == '__main__':
    main()
