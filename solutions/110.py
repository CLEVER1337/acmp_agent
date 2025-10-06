
def main():
    import sys
    n, k = map(int, sys.stdin.readline().split())
    k_char = str(k)
    
    if k == 0:
        print(n)
        return
        
    def is_valid(num_str):
        if '.' in num_str:
            integer_part, fractional_part = num_str.split('.', 1)
            if '(' in fractional_part:
                fractional_part = fractional_part.split('(', 1)[0]
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
            
    def generate_numbers():
        numbers = set()
        max_len = min(12, len(str(n)) + 2)
        
        for length in range(1, max_len + 1):
            for num in range(10 ** length):
                s = str(num).zfill(length)
                if all(c in ['0', k_char] for c in s):
                    if s.lstrip('0'):
                        numbers.add(int(s))
        
        numbers = sorted(numbers, reverse=True)
        return numbers
        
    def find_min_terms(target):
        numbers = generate_numbers()
        dp = [float('inf')] * (target + 1)
        prev = [-1] * (target + 1)
        dp[0] = 0
        
        for i in range(1, target + 1):
            for num in numbers:
                if num <= i and dp[i - num] + 1 < dp[i]:
                    dp[i] = dp[i - num] + 1
                    prev[i] = num
                    
        result = []
        current = target
        while current > 0:
            num = prev[current]
            result.append(str(num))
            current -= num
            
        return result
        
    result_terms = find_min_terms(n)
    output = f"{n}={'+'.join(result_terms)}"
    print(output)

if __name__ == "__main__":
    main()
