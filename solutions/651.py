
import math
from collections import deque

def min_operations(N, M):
    if N == M:
        return 0
        
    if M % N != 0:
        return -1
        
    target = M // N
    
    factors = []
    temp = target
    for i in range(2, int(math.isqrt(target)) + 1):
        while temp % i == 0:
            factors.append(i)
            temp //= i
    if temp > 1:
        factors.append(temp)
    
    for factor in factors:
        if factor != 2 and factor != 3:
            return -1
            
    return len(factors)

def main():
    with open('INPUT.TXT', 'r') as f:
        N, M = map(int, f.readline().split())
    
    result = min_operations(N, M)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
