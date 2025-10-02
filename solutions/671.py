
def main():
    with open('INPUT.TXT', 'r') as f:
        n_str = f.readline().strip()
    
    length = len(n_str)
    count = 0
    
    for i in range(1, length):
        count += 2 ** i
    
    def dfs(pos, tight, current):
        if pos == length:
            if current <= n_str:
                return 1
            return 0
        
        limit = int(n_str[pos]) if tight else 9
        total = 0
        
        for digit in [4, 7]:
            if digit > limit:
                continue
            new_tight = tight and (digit == limit)
            new_current = current + str(digit)
            total += dfs(pos + 1, new_tight, new_current)
        
        return total
    
    result = count + dfs(0, True, '')
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
