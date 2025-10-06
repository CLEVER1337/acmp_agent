
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    if n == 1:
        result = a[0]
        print(result)
        return
        
    total_xor_a = 0
    for num in a:
        total_xor_a ^= num
        
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ a[i]
        
    def f(x, y):
        if x == y:
            return -1
        diff = abs(x - y)
        if diff == 0:
            return -1
        power = 0
        while diff % 2 == 0:
            diff //= 2
            power += 1
        return power - 1
        
    def compute_bi(i):
        res = 0
        for j in range(i + 1, n):
            res ^= f(a[i], a[j])
        return res
        
    if n <= 1000:
        total_b_xor = 0
        for i in range(n - 1):
            bi = compute_bi(i)
            total_b_xor ^= bi
            
        result = total_xor_a ^ total_b_xor
        print(result)
        return
        
    from collections import defaultdict
    bits = [defaultdict(int) for _ in range(33)]
    
    total_b_xor = 0
    for i in range(n - 1, -1, -1):
        num = a[i]
        current = 0
        for bit in range(0, 33):
            mask = (1 << bit) - 1
            low_bits = num & mask
            count = bits[bit].get(low_bits, 0)
            if count % 2 == 1:
                current ^= (bit - 1)
                
        total_b_xor ^= current
        
        for bit in range(0, 33):
            mask = (1 << bit) - 1
            low_bits = num & mask
            bits[bit][low_bits] = bits[bit].get(low_bits, 0) + 1
                
    result = total_xor_a ^ total_b_xor
    print(result)

if __name__ == "__main__":
    main()
