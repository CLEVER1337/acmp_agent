
def char_to_value(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def convert_to_decimal(s, base):
    try:
        result = 0
        for char in s:
            digit = char_to_value(char)
            if digit >= base:
                return -1
            result = result * base + digit
            if result > 10**7:
                return -1
        return result
    except:
        return -1

def solve():
    with open('INPUT.TXT', 'r') as f:
        A = f.readline().strip()
        B = int(f.readline().strip())
    
    max_digit = 0
    for char in A:
        digit = char_to_value(char)
        if digit > max_digit:
            max_digit = digit
    
    min_base = max_digit + 1
    if min_base < 2:
        min_base = 2
    
    left, right = min_base, max(10**7 + 1, min_base + 1)
    solution = 0
    
    while left <= right:
        mid = (left + right) // 2
        decimal_val = convert_to_decimal(A, mid)
        if decimal_val == -1 or decimal_val > B:
            right = mid - 1
        elif decimal_val < B:
            left = mid + 1
        else:
            solution = mid
            right = mid - 1
    
    if solution != 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(str(solution))
        return
    
    for base in range(min_base, 37):
        decimal_val = convert_to_decimal(A, base)
        if decimal_val == B:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(str(base))
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('0')

solve()
