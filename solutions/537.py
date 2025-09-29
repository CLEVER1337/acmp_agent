
import sys
import math
from functools import lru_cache

sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    M = int(data[1])
    K = int(data[2])
    numbers = list(map(int, data[3:3+n]))
    
    numbers.sort()
    
    @lru_cache(maxsize=None)
    def dp(mask, last):
        if mask == (1 << n) - 1:
            return 1
            
        total = 0
        for i in range(n):
            if not (mask & (1 << i)):
                if last is None or math.gcd(numbers[last], numbers[i]) >= K:
                    total += dp(mask | (1 << i), i)
        return total
    
    def find_mth_permutation():
        mask = 0
        last = None
        m = M
        result = []
        
        for pos in range(n):
            found = False
            for i in range(n):
                if mask & (1 << i):
                    continue
                    
                if last is None or math.gcd(numbers[last], numbers[i]) >= K:
                    count = dp(mask | (1 << i), i)
                    if m <= count:
                        result.append(numbers[i])
                        mask |= (1 << i)
                        last = i
                        found = True
                        break
                    else:
                        m -= count
            if not found:
                return None
                
        return result
    
    total_permutations = dp(0, None)
    if M > total_permutations:
        print(-1)
    else:
        permutation = find_mth_permutation()
        if permutation:
            print(" ".join(map(str, permutation)))
        else:
            print(-1)

if __name__ == "__main__":
    main()
