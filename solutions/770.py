
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

def decrypt(s):
    n = len(s)
    groups = []
    left, right = 0, n - 1
    group_num = 1
    
    while left <= right:
        if group_num % 2 == 1:
            size = min(group_num, right - left + 1)
            groups.append(s[left:left + size])
            left += size
        else:
            size = min(group_num, right - left + 1)
            start = right - size + 1
            groups.append(s[start:right + 1])
            right -= size
        group_num += 1
    
    decrypted = [''] * n
    pos = 0
    for i in range(0, len(groups), 2):
        if i + 1 < len(groups):
            decrypted[pos:pos + len(groups[i + 1])] = groups[i + 1]
            pos += len(groups[i + 1])
            decrypted[pos:pos + len(groups[i])] = groups[i]
            pos += len(groups[i])
        else:
            decrypted[pos:pos + len(groups[i])] = groups[i]
            pos += len(groups[i])
    
    return ''.join(decrypted)

def main():
    with open('INPUT.TXT', 'r') as f:
        encrypted = f.read().strip()
    
    if not encrypted:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Impossible')
        return
    
    decrypted = decrypt(encrypted)
    n = len(decrypted)
    
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    
    if not primes:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Impossible')
        return
    
    result = []
    for pos in primes:
        if pos - 1 < len(decrypted):
            result.append(decrypted[pos - 1])
    
    if not result:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Impossible')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(''.join(result))

if __name__ == '__main__':
    main()
