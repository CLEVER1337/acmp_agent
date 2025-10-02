
import sys

def solve():
    data = sys.stdin.read().split()
    index = 0
    output_lines = []
    while index < len(data):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        if n == 0 and k == 0:
            break
            
        if k == 1:
            output_lines.append("1")
            continue
            
        if n < k:
            output_lines.append("-1")
            continue
            
        def lex_min():
            if k <= n:
                candidate = k
                min_lex = str(candidate)
                
                length = len(str(k))
                prefix = str(k)
                
                for l in range(length, len(str(n)) + 1):
                    low = 10**(l-1)
                    high = min(n, 10**l - 1)
                    
                    if low > n:
                        break
                        
                    start = (low + k - 1) // k * k
                    if start > high:
                        continue
                        
                    num_str = str(start)
                    if len(num_str) == l:
                        if num_str < min_lex:
                            min_lex = num_str
                            
                    if l > length:
                        for first_digit in range(1, 10):
                            base = first_digit * (10**(l-1))
                            remainder = base % k
                            if remainder == 0:
                                candidate_num = base
                            else:
                                candidate_num = base + (k - remainder)
                                
                            if candidate_num <= high and candidate_num >= low:
                                num_str = str(candidate_num)
                                if num_str < min_lex:
                                    min_lex = num_str
                
                return min_lex
            return "-1"
            
        result = lex_min()
        output_lines.append(result)
    
    sys.stdout.write("\n".join(output_lines))

solve()
