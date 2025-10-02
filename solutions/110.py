
def main():
    import sys
    n, k = map(int, sys.stdin.readline().split())
    k_char = str(k)
    
    if n == 0:
        print("0")
        return
        
    def is_beautiful(num_str):
        if '.' in num_str:
            integer_part, fractional_part = num_str.split('.', 1)
            if '(' in fractional_part:
                fractional_part = fractional_part.split('(')[0]
            for c in integer_part:
                if c != '0' and c != k_char:
                    return False
            for c in fractional_part:
                if c != '0' and c != k_char:
                    return False
            return True
        else:
            for c in num_str:
                if c != '0' and c != k_char:
                    return False
            return True
            
    def minimize_fraction(s):
        if '.' not in s:
            return s
            
        integer_part, fractional_part = s.split('.', 1)
        
        if '(' in fractional_part:
            preperiod, period_part = fractional_part.split('(', 1)
            period = period_part.rstrip(')')
            
            if all(c == '0' for c in period):
                if all(c == '0' for c in preperiod):
                    return integer_part
                else:
                    return integer_part + '.' + preperiod.rstrip('0')
                    
            if period == k_char * len(period):
                period = k_char
                
            if preperiod.endswith(period):
                preperiod = preperiod[:-len(period)]
                period = period
                
            if preperiod == '':
                return integer_part + '.(' + period + ')'
            else:
                return integer_part + '.' + preperiod + '(' + period + ')'
        else:
            if fractional_part.rstrip('0') == '':
                return integer_part
            else:
                return integer_part + '.' + fractional_part.rstrip('0')
                
    def generate_beautiful_numbers(max_count=10):
        beautiful_nums = []
        
        for length in range(1, 15):
            for num in range(10 ** length):
                num_str = str(num).zfill(length)
                if all(c in ['0', k_char] for c in num_str):
                    if num_str[0] != '0':
                        beautiful_nums.append(int(num_str))
                        
        beautiful_nums = sorted(set(beautiful_nums))
        return [x for x in beautiful_nums if x > 0][:max_count]
        
    beautiful_ints = generate_beautiful_numbers(100)
    
    dp = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for num in beautiful_ints:
            if num <= i:
                if dp[i - num] + 1 < dp[i]:
                    dp[i] = dp[i - num] + 1
                    prev[i] = num
                    
    if dp[n] != float('inf'):
        result = []
        current = n
        while current > 0:
            num = prev[current]
            result.append(str(num))
            current -= num
        print(f"{n}={'+'.join(result)}")
        return
        
    for num in beautiful_ints:
        if n % num == 0:
            count = n // num
            result = [str(num)] * count
            print(f"{n}={'+'.join(result)}")
            return
            
    beautiful_ints_desc = sorted(beautiful_ints, reverse=True)
    result = []
    remaining = n
    
    for num in beautiful_ints_desc:
        while remaining >= num:
            count = remaining // num
            result.extend([str(num)] * count)
            remaining -= num * count
            
    if remaining == 0:
        print(f"{n}={'+'.join(result)}")
        return
        
    result = [str(n)]
    print(f"{n}={n}")

if __name__ == "__main__":
    main()
