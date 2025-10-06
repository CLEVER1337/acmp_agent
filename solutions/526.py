
def char_to_value(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def convert_to_decimal(s, base):
    num = 0
    for char in s:
        digit = char_to_value(char)
        if digit >= base:
            return -1
        num = num * base + digit
        if num > 10**7:
            return -1
    return num

def find_min_base(s):
    min_base = 2
    for char in s:
        digit = char_to_value(char)
        min_base = max(min_base, digit + 1)
    return min_base

def main():
    with open('INPUT.TXT', 'r') as f:
        A = f.readline().strip()
        B = int(f.readline().strip())
    
    min_possible_base = find_min_base(A)
    left = min_possible_base
    right = 36
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
    
    if solution == 0:
        for base in range(min_possible_base, 37):
            if convert_to_decimal(A, base) == B:
                solution = base
                break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(solution))

if __name__ == "__main__":
    main()
