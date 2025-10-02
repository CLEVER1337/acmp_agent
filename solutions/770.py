
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def decrypt(s):
    n = len(s)
    groups = []
    left = 0
    right = n - 1
    group_num = 1
    
    while left <= right:
        if group_num % 2 == 1:
            size = min(group_num, right - left + 1)
            groups.append(s[left:left+size])
            left += size
        else:
            size = min(group_num, right - left + 1)
            groups.append(s[right-size+1:right+1])
            right -= size
        group_num += 1
    
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
    
    result = []
    current = []
    in_word = False
    
    for i, char in enumerate(decrypted):
        if char.isupper():
            if in_word and current:
                result.append(''.join(current))
            current = [char]
            in_word = True
        elif char.islower() and in_word:
            current.append(char)
        else:
            if current:
                result.append(''.join(current))
            current = []
            in_word = False
    
    if current:
        result.append(''.join(current))
    
    if not result:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Impossible')
        return
    
    primes = [i+1 for i in range(n) if is_prime(i+1)]
    final_result = []
    
    for pos in primes:
        if pos > len(result):
            break
        word_start = 0
        for word in result:
            word_end = word_start + len(word)
            if word_start < pos <= word_end:
                final_result.append(word)
                break
            word_start = word_end
    
    if not final_result:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Impossible')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(''.join(final_result))

if __name__ == '__main__':
    main()
