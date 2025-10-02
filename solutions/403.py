
def count_up_to(n):
    s = str(n)
    length = len(s)
    count = 0
    freq = {}
    
    def dfs(pos, tight, leading_zero):
        if pos == length:
            if leading_zero:
                return 0
            for digit in freq:
                if freq[digit] > 2:
                    return 0
            return 1
            
        limit = int(s[pos]) if tight else 9
        total = 0
        
        for d in range(0, limit + 1):
            new_tight = tight and (d == limit)
            new_leading_zero = leading_zero and (d == 0)
            
            if not new_leading_zero:
                freq[d] = freq.get(d, 0) + 1
                
            if freq.get(d, 0) <= 2:
                total += dfs(pos + 1, new_tight, new_leading_zero)
                
            if not new_leading_zero:
                freq[d] -= 1
                if freq[d] == 0:
                    del freq[d]
                    
        return total
    
    return dfs(0, True, True)

def main():
    with open("INPUT.TXT", "r") as f:
        L, R = map(int, f.readline().split())
    
    result = count_up_to(R) - count_up_to(L - 1)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
