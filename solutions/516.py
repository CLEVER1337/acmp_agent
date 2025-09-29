
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with open('INPUT.TXT', 'r') as f:
        n = f.readline().strip()
    
    digits = sorted(n)
    ascending_num = int(''.join(digits))
    descending_num = int(''.join(reversed(digits)))
    
    if is_prime(ascending_num) and is_prime(descending_num):
        result = 'Yes'
    else:
        result = 'No'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
