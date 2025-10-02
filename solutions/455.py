
def main():
    with open('INPUT.TXT', 'r') as f:
        q_str = f.readline().strip()
        n = int(f.readline().strip())
    
    if '(' not in q_str:
        integer_part, fractional_part = q_str.split('.')
        result = str(int(integer_part + fractional_part) * n)
        if len(result) <= len(fractional_part):
            result = '0.' + result.zfill(len(fractional_part))[-len(fractional_part):]
        else:
            result = result[:-len(fractional_part)] + '.' + result[-len(fractional_part):]
        with open('OUTPUT.TXT', 'w') as f:
            f.write(result.rstrip('0').rstrip('.'))
        return
    
    non_period_start = q_str.find('(')
    non_period_end = q_str.find(')')
    integer_part = q_str.split('.')[0]
    non_repeating = q_str.split('.')[1].split('(')[0]
    repeating = q_str[non_period_start+1:non_period_end]
    
    full_non_repeating = non_repeating + repeating
    k = len(repeating)
    m = len(non_repeating)
    
    numerator = int(integer_part + full_non_repeating) - int(integer_part + non_repeating)
    denominator = (10**(m+k) - 10**m)
    
    numerator *= n
    gcd_val = gcd(numerator, denominator)
    numerator //= gcd_val
    denominator //= gcd_val
    
    integer_part_result = numerator // denominator
    numerator %= denominator
    
    if numerator == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(str(integer_part_result))
        return
    
    denominators = []
    while denominator % 2 == 0:
        denominators.append(2)
        denominator //= 2
    while denominator % 5 == 0:
        denominators.append(5)
        denominator //= 5
    
    non_period_len = len(denominators)
    period_denom = denominator
    
    digits = []
    rem = numerator
    seen = {}
    period_start = -1
    
    for i in range(1000):
        rem *= 10
        digit = rem // period_denom
        digits.append(str(digit))
        rem %= period_denom
        
        if rem == 0:
            break
            
        if rem in seen:
            period_start = seen[rem]
            break
            
        seen[rem] = i
    
    non_period_digits = digits[:non_period_len]
    period_digits = digits[non_period_len:]
    
    if period_start != -1 and period_start >= non_period_len:
        period_digits = digits[non_period_len:period_start] + digits[period_start:]
    
    result_str = str(integer_part_result) + '.'
    if non_period_digits:
        result_str += ''.join(non_period_digits)
    if period_digits:
        result_str += '(' + ''.join(period_digits) + ')'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result_str)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    main()
