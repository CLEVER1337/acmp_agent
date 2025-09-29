
def count_numbers(L, R):
    def can_form(n):
        s = str(n)
        count = [0] * 10
        for char in s:
            digit = int(char)
            count[digit] += 1
            if count[digit] > 2:
                return False
        return True
    
    def dfs(pos, tight, leading_zero, count, digits):
        if pos == len(digits):
            return 1
        
        limit = int(digits[pos]) if tight else 9
        total = 0
        
        for d in range(0, limit + 1):
            new_tight = tight and (d == limit)
            new_leading_zero = leading_zero and (d == 0)
            
            if new_leading_zero:
                total += dfs(pos + 1, new_tight, new_leading_zero, count, digits)
            else:
                if count[d] < 2:
                    count[d] += 1
                    total += dfs(pos + 1, new_tight, new_leading_zero, count, digits)
                    count[d] -= 1
                    
        return total
    
    def count_up_to(n):
        if n < 0:
            return 0
        digits = list(str(n))
        count = [0] * 10
        return dfs(0, True, True, count, digits)
    
    return count_up_to(R) - count_up_to(L - 1)

def main():
    with open('INPUT.TXT', 'r') as f:
        L, R = map(int, f.read().split())
    result = count_numbers(L, R)
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
