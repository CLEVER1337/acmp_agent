
def multiply_large_numbers(a, b):
    if a == '0' or b == '0':
        return '0'
    
    len_a, len_b = len(a), len(b)
    result = [0] * (len_a + len_b)
    
    for i in range(len_a - 1, -1, -1):
        carry = 0
        digit_a = int(a[i])
        
        for j in range(len_b - 1, -1, -1):
            digit_b = int(b[j])
            temp = digit_a * digit_b + result[i + j + 1] + carry
            result[i + j + 1] = temp % 10
            carry = temp // 10
        
        result[i] += carry
    
    start_index = 0
    while start_index < len(result) - 1 and result[start_index] == 0:
        start_index += 1
    
    return ''.join(map(str, result[start_index:]))

with open('INPUT.TXT', 'r') as f:
    M = f.readline().strip()
    N = f.readline().strip()

product = multiply_large_numbers(M, N)

with open('OUTPUT.TXT', 'w') as f:
    f.write(product)
