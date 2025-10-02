
def next_number_with_same_popcount(n):
    if n == 0:
        return 1
    
    c = n
    c0 = 0
    c1 = 0
    
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1
        
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
        
    p = c0 + c1
    
    if p == 31 or p == 0:
        return None
        
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1
    
    return n

with open('INPUT.TXT', 'r') as f:
    n = int(f.read().strip())
    
result = next_number_with_same_popcount(n)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
