
def main():
    import sys
    n, k = map(int, sys.stdin.readline().split())
    k_char = str(k)
    
    def is_beautiful(num_str):
        if '.' in num_str:
            integer_part, fractional_part = num_str.split('.', 1)
            if '(' in fractional_part:
                fractional_part = fractional_part.split('(')[0]
            for char in integer_part:
                if char != '0' and char != k_char:
                    return False
            for char in fractional_part:
                if char != '0' and char != k_char:
                    return False
            return True
        else:
            for char in num_str:
                if char != '0' and char != k_char:
                    return False
            return True
    
    def format_number(num):
        if num == 0:
            return "0"
        if num.is_integer():
            return str(int(num))
        
        s = str(num)
        if 'e' in s or 'E' in s:
            return s
        
        if '.' in s:
            parts = s.split('.')
            integer_part = parts[0]
            fractional_part = parts[1]
            
            if fractional_part == '0':
                return integer_part
            
            if all(c == '0' for c in fractional_part):
                return integer_part
            
            return s.rstrip('0').rstrip('.')
        return s
    
    def generate_beautiful_numbers(max_count=100):
        beautiful_nums = []
        
        for length in range(1, 15):
            for num_zeros in range(length):
                num_str = k_char + '0' * num_zeros
                if num_str:
                    num = int(num_str)
                    if num > 0:
                        beautiful_nums.append(num)
        
        for integer_part_len in range(1, 8):
            for fractional_part_len in range(1, 8):
                for integer_zeros in range(integer_part_len):
                    for fractional_zeros in range(fractional_part_len):
                        integer_part = k_char + '0' * integer_zeros
                        fractional_part = '0' * fractional_zeros + k_char
                        num_str = integer_part + '.' + fractional_part
                        num = float(num_str)
                        if num > 0:
                            beautiful_nums.append(num)
        
        beautiful_nums = sorted(set(beautiful_nums), reverse=True)
        return beautiful_nums[:max_count]
    
    beautiful_numbers = generate_beautiful_numbers(200)
    
    dp = [None] * (n + 1)
    dp[0] = (0, [])
    
    for i in range(1, n + 1):
        min_count = float('inf')
        best_combination = None
        
        for num in beautiful_numbers:
            if num <= i:
                prev = i - num
                if dp[prev] is not None:
                    count = dp[prev][0] + 1
                    if count < min_count:
                        min_count = count
                        best_combination = dp[prev][1] + [num]
        
        if best_combination is not None:
            dp[i] = (min_count, best_combination)
    
    if dp[n] is not None:
        result = dp[n][1]
        formatted_result = []
        for num in result:
            formatted_result.append(format_number(num))
        
        output = f"{n}={'+'.join(formatted_result)}"
        print(output)
    else:
        result = []
        remaining = n
        while remaining > 0:
            for num in beautiful_numbers:
                if num <= remaining:
                    result.append(num)
                    remaining -= num
                    break
        
        formatted_result = []
        for num in result:
            formatted_result.append(format_number(num))
        
        output = f"{n}={'+'.join(formatted_result)}"
        print(output)

if __name__ == "__main__":
    main()
