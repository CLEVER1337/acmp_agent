
def char_to_value(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def convert_number(s, base):
    if base == 1:
        return len(s)
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
    
    min_base = 1
    for char in A:
        value = char_to_value(char)
        min_base = max(min_base, value + 1)
    
    left, right = min_base, max(min_base, B + 1)
    found_base = 0
    
    if convert_number(A, min_base) == B:
        found_base = min_base
    
    if found_base == 0:
        while left <= right:
            mid = (left + right) // 2
            converted = convert_number(A, mid)
            if converted == B:
                found_base = mid
                right = mid - 1
            elif converted == -1 or converted > B:
                right = mid - 1
            else:
                left = mid + 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(found_base))

solve()
