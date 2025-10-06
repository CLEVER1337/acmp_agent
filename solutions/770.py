
import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    data = sys.stdin.read().strip()
    if not data:
        print("Impossible")
        return
        
    n = len(data)
    groups = []
    left = 0
    right = n - 1
    group_id = 1
    
    while left <= right:
        if group_id % 2 == 1:
            take = min(group_id, right - left + 1)
            groups.append(data[left:left+take])
            left += take
        else:
            take = min(group_id, right - left + 1)
            groups.append(data[right-take+1:right+1])
            right -= take
        group_id += 1
        
    decrypted = [''] * n
    pos = 0
    for i in range(0, len(groups), 2):
        if i + 1 < len(groups):
            decrypted[pos:pos+len(groups[i+1])] = groups[i+1]
            pos += len(groups[i+1])
            decrypted[pos:pos+len(groups[i])] = groups[i]
            pos += len(groups[i])
        else:
            decrypted[pos:pos+len(groups[i])] = groups[i]
            pos += len(groups[i])
            
    original = ''.join(decrypted)
    
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
            
    if not primes:
        print("Impossible")
        return
        
    result = []
    for idx in primes:
        if idx - 1 < len(original):
            result.append(original[idx-1])
            
    if not result:
        print("Impossible")
    else:
        print(''.join(result))

if __name__ == "__main__":
    main()
