
import sys
from math import gcd
from functools import reduce

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    m = int(data[1])
    n = list(map(int, data[2:2+m]))
    
    a = [0] * k
    used = [set() for _ in range(k)]
    
    for i in range(m):
        if i == 0:
            continue
            
        prev = n[i-1]
        curr = n[i]
        
        if prev == curr:
            continue
            
        ratio = prev // curr
        for j in range(k):
            if ratio > 1 and a[j] == 0:
                a[j] = ratio
                break
                
    for i in range(k):
        if a[i] == 0:
            a[i] = 2
            
    print(' '.join(map(str, a)))

if __name__ == "__main__":
    main()
