
def main():
    n = int(input().strip())
    if n == 1:
        print("10 0")
        return
        
    count = 0
    min_num = float('inf')
    
    def dfs(digits, current_sum, current_prod, num, pos):
        nonlocal count, min_num
        
        if pos == n:
            if current_sum == current_prod and current_prod != 0:
                count += 1
                min_num = min(min_num, num)
            return
            
        start = 1 if pos == 0 else 0
        
        for d in range(start, 10):
            new_sum = current_sum + d
            new_prod = current_prod * d if current_prod != 0 else d
            new_num = num * 10 + d
            
            if new_prod == 0:
                continue
                
            if new_prod > new_sum + (n - pos - 1) * 9:
                continue
                
            dfs(digits, new_sum, new_prod, new_num, pos + 1)
    
    dfs([], 0, 0, 0, 0)
    print(f"{count} {min_num}")

if __name__ == "__main__":
    main()
