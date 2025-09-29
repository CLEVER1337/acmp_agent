
with open('INPUT.TXT', 'r') as f:
    a = f.readline().strip()
    b = f.readline().strip()

def subtract_large_numbers(a, b):
    if len(a) < len(b) or (len(a) == len(b) and a < b):
        return '-' + subtract_large_numbers(b, a)
    
    result = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0:
        digit_a = int(a[i])
        digit_b = int(b[j]) if j >= 0 else 0
        
        diff = digit_a - digit_b - carry
        
        if diff < 0:
            diff += 10
            carry = 1
        else:
            carry = 0
            
        result.append(str(diff))
        
        i -= 1
        j -= 1
    
    result_str = ''.join(result[::-1]).lstrip('0')
    return result_str if result_str else '0'

result = subtract_large_numbers(a, b)
with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
