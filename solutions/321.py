
def convert(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while n > 0:
        result.append(digits[n % base])
        n //= base
    return ''.join(reversed(result))

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    results = []
    for base in range(2, 37):
        converted = convert(n, base)
        if len(converted) == len(set(converted)):
            results.append(str(base))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(results))

if __name__ == '__main__':
    main()
