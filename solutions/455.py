
def main():
    with open("INPUT.TXT", "r") as f:
        q_str = f.readline().strip()
        n = int(f.readline().strip())
    
    if '(' not in q_str:
        integer_part_str, fractional_part_str = q_str.split('.') if '.' in q_str else (q_str, '0')
        fractional_part_str = fractional_part_str.rstrip('0')
        if fractional_part_str == '':
            result = str(int(integer_part_str) * n)
            with open("OUTPUT.TXT", "w") as f:
                f.write(result)
            return
        
        numerator = int(integer_part_str + fractional_part_str)
        denominator = 10 ** len(fractional_part_str)
        numerator = numerator * n
        gcd_val = gcd(numerator, denominator)
        numerator //= gcd_val
        denominator //= gcd_val
        
        if denominator == 1:
            with open("OUTPUT.TXT", "w") as f:
                f.write(str(numerator))
        else:
            integer_part = numerator // denominator
            fractional_part = numerator % denominator
            with open("OUTPUT.TXT", "w") as f:
                f.write(f"{integer_part}.{fractional_part:0{len(str(denominator))-1}}")
        return
    
    dot_index = q_str.index('.')
    open_bracket = q_str.index('(')
    close_bracket = q_str.index(')')
    
    non_periodic = q_str[dot_index+1:open_bracket]
    periodic = q_str[open_bracket+1:close_bracket]
    
    integer_part_str = q_str[:dot_index]
    
    k = len(non_periodic)
    l = len(periodic)
    
    a = int(integer_part_str + non_periodic + periodic) if non_periodic != '' else int(integer_part_str + periodic)
    b = int(integer_part_str + non_periodic) if non_periodic != '' else int(integer_part_str)
    
    numerator = a - b
    denominator = (10 ** (k + l)) - (10 ** k)
    
    numerator *= n
    gcd_val = gcd(numerator, denominator)
    numerator //= gcd_val
    denominator //= gcd_val
    
    if denominator == 1:
        with open("OUTPUT.TXT", "w") as f:
            f.write(str(numerator))
        return
    
    integer_part = numerator // denominator
    fractional = numerator % denominator
    
    if fractional == 0:
        with open("OUTPUT.TXT", "w") as f:
            f.write(str(integer_part))
        return
    
    digits = []
    remainder = fractional
    remainders_seen = {}
    period_start = -1
    period_digits = []
    non_periodic_digits = []
    
    while remainder != 0:
        if remainder in remainders_seen:
            period_start = remainders_seen[remainder]
            non_periodic_digits = digits[:period_start]
            period_digits = digits[period_start:]
            break
        
        remainders_seen[remainder] = len(digits)
        remainder *= 10
        digit = remainder // denominator
        digits.append(digit)
        remainder %= denominator
    else:
        non_periodic_digits = digits
        period_digits = []
    
    result_str = str(integer_part) + '.'
    if non_periodic_digits:
        result_str += ''.join(str(d) for d in non_periodic_digits)
    
    if period_digits:
        result_str += '(' + ''.join(str(d) for d in period_digits) + ')'
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(result_str)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    main()
