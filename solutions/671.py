
def main():
    n_str = input().strip()
    length = len(n_str)
    count = 0
    
    for i in range(1, length):
        count += 2 ** i
    
    def dfs(pos, tight, path):
        if pos == length:
            return 1
        
        total = 0
        limit = int(n_str[pos]) if tight else 9
        
        for digit in [4, 7]:
            if digit <= limit:
                new_tight = tight and (digit == limit)
                total += dfs(pos + 1, new_tight, path + str(digit))
        
        return total
    
    result = count + dfs(0, True, "")
    print(result)

if __name__ == "__main__":
    main()
