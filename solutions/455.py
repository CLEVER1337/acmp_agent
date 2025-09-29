
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_to_fraction(s):
    if '(' not in s:
        integer_part = s.split('.')[0]
        non_periodic = s.split('.')[1] if '.' in s else ''
        return integer_part, non_periodic, ''
    
    parts = s.split('(')
    integer_part = parts[0].split('.')[0]
    decimal_parts = parts[0].split('.')[1] if '.' in parts[0] else ''
    periodic_part = parts[1].rstrip(')')
    
    return integer_part, decimal_parts, periodic_part

def fraction_to_rational(integer_part, non_periodic, periodic):
    a = integer_part
    b = non_periodic
    c = periodic
    
    full_non_periodic = a + b
    if full_non_periodic == '':
        full_non_periodic = '0'
    
    k = len(b)
    m = len(c)
    
    numerator1 = int(full_non_periodic + c) - int(full_non_periodic)
    denominator1 = 10**k * (10**m - 1)
    
    return numerator1, denominator1

def simplify_fraction(numerator, denominator):
    g = gcd(numerator, denominator)
    return numerator // g, denominator // g

def process_multiplication(q_str, n):
    integer_part, non_periodic, periodic = convert_to_fraction(q_str)
    
    if periodic == '':
        if non_periodic == '':
            result = int(integer_part) * n
            return str(result)
        else:
            decimal_num = integer_part + non_periodic
            result_int = int(decimal_num) * n
            result_str = str(result_int)
            dec_len = len(non_periodic)
            if len(result_str) > dec_len:
                integer_part_result = result_str[:-dec_len]
                fractional_part = result_str[-dec_len:]
                if fractional_part != '0':
                    return integer_part_result + '.' + fractional_part
                else:
                    return integer_part_result
            else:
                fractional_part = result_str.zfill(dec_len)
                return '0.' + fractional_part
    
    numerator, denominator = fraction_to_rational(integer_part, non_periodic, periodic)
    numerator *= n
    numerator, denominator = simplify_fraction(numerator, denominator)
    
    integer_result = numerator // denominator
    remainder = numerator % denominator
    
    if remainder == 0:
        return str(integer_result)
    
    numerator = remainder
    denominator_orig = denominator
    
    factors_2 = 0
    factors_5 = 0
    temp = denominator
    while temp % 2 == 0:
        factors_2 += 1
        temp //= 2
    while temp % 5 == 0:
        factors_5 += 1
        temp //= 5
    
    non_periodic_length = max(factors_2, factors_5)
    periodic_denominator = temp
    
    if periodic_denominator == 1:
        decimal_part = numerator * (10**non_periodic_length) // denominator_orig
        decimal_str = str(decimal_part).zfill(non_periodic_length)
        return str(integer_result) + '.' + decimal_str
    
    non_periodic_numerator = numerator
    non_periodic_denom = denominator_orig
    for _ in range(non_periodic_length):
        non_periodic_numerator *= 10
        non_periodic_part = non_periodic_numerator // non_periodic_denom
        non_periodic_numerator %= non_periodic_denom
    
    periodic_numerator = non_periodic_numerator
    periodic_denom = periodic_denominator
    
    digits = []
    seen = {}
    index = 0
    
    while periodic_numerator not in seen and periodic_numerator != 0:
        seen[periodic_numerator] = index
        periodic_numerator *= 10
        digit = periodic_numerator // periodic_denom
        digits.append(str(digit))
        periodic_numerator %= periodic_denom
        index += 1
    
    if periodic_numerator == 0:
        decimal_part = numerator * (10**non_periodic_length) // denominator_orig
        decimal_str = str(decimal_part).zfill(non_periodic_length)
        return str(integer_result) + '.' + decimal_str
    
    start_index = seen[periodic_numerator]
    non_periodic_digits = digits[:start_index]
    periodic_digits = digits[start_index:]
    
    decimal_value = numerator * (10**non_periodic_length) // denominator_orig
    decimal_str = str(decimal_value).zfill(non_periodic_length)
    
    if non_periodic_digits:
        decimal_str += ''.join(non_periodic_digits)
    
    if decimal_str == '':
        decimal_str = '0'
    
    result = str(integer_result) + '.' + decimal_str
    if periodic_digits:
        result += '(' + ''.join(periodic_digits) + ')'
    
    return result

def main():
    with open('INPUT.TXT', 'r') as f:
        q_str = f.readline().strip()
        n = int(f.readline().strip())
    
    result = process_multiplication(q_str, n)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
