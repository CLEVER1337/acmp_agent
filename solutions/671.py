
def main():
    n = input().strip()
    length = len(n)
    count = 0
    
    for i in range(1, length):
        count += 2 ** i
    
    def dfs(pos, tight):
        if pos == length:
            return 1
        
        limit = int(n[pos]) if tight else 9
        total = 0
        
        for digit in [4, 7]:
            if digit <= limit:
                new_tight = tight and (digit == limit)
                total += dfs(pos + 1, new_tight)
        
        return total
    
    count += dfs(0, True)
    print(count)

if __name__ == "__main__":
    main()
