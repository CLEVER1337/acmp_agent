
import sys

def max_power_two(x):
    if x == 0:
        return -1
    count = 0
    while x % 2 == 0:
        count += 1
        x //= 2
    return count

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    total_xor = 0
    for num in a:
        total_xor ^= num
        
    if n == 1:
        print(total_xor)
        return
        
    result = total_xor
    bits = 32
    
    for k in range(bits):
        mask = (1 << k)
        count_ones = 0
        
        for i in range(n):
            if a[i] & mask:
                count_ones += 1
        
        pairs_with_bit = count_ones * (n - count_ones)
        if pairs_with_bit % 2 == 1:
            result ^= mask
            
    print(result)

if __name__ == "__main__":
    main()
