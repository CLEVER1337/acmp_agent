
def roman_to_int(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_map.get(char, 0)
        if value == 0:
            return -1
        
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    
    return result

def int_to_roman(n):
    if n <= 0:
        return ""
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syms[i]
            n -= val[i]
        i += 1
    return roman_num

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        with open('INPUT.TXT', 'r') as f:
            data = f.readline().strip()
        
        if '/' not in data:
            with open('OUTPUT.TXT', 'w') as f:
                f.write("ERROR")
            return
        
        parts = data.split('/')
        if len(parts) != 2:
            with open('OUTPUT.TXT', 'w') as f:
                f.write("ERROR")
            return
        
        numerator_str, denominator_str = parts
        
        numerator = roman_to_int(numerator_str)
        denominator = roman_to_int(denominator_str)
        
        if numerator == -1 or denominator == -1 or numerator <= 0 or denominator <= 0:
            with open('OUTPUT.TXT', 'w') as f:
                f.write("ERROR")
            return
        
        common_divisor = gcd(numerator, denominator)
        simplified_num = numerator // common_divisor
        simplified_den = denominator // common_divisor
        
        if simplified_den == 1:
            result = int_to_roman(simplified_num)
        else:
            result = f"{int_to_roman(simplified_num)}/{int_to_roman(simplified_den)}"
        
        with open('OUTPUT.TXT', 'w') as f:
            f.write(result)
            
    except Exception:
        with open('OUTPUT.TXT', 'w') as f:
            f.write("ERROR")

if __name__ == "__main__":
    main()
