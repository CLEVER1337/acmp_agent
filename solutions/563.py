
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    if n == 1:
        print(a[0])
        return
        
    total_xor = 0
    for num in a:
        total_xor ^= num
        
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] ^ a[i]
        
    result = 0
    for k in range(31, -1, -1):
        bit_mask = 1 << k
        count = 0
        
        for i in range(n):
            if a[i] & bit_mask:
                count += 1
                
        if count % 2 == 1:
            result |= bit_mask
            
    for k in range(31, -1, -1):
        bit_mask = 1 << k
        cnt = 0
        
        for i in range(n):
            if a[i] & bit_mask:
                cnt += n - 1 - i
            else:
                cnt += i
                
        if cnt % 2 == 1:
            result ^= bit_mask
            
    print(result)

if __name__ == "__main__":
    main()
