
def has_duplicate_digits(n):
    digits = set()
    for d in str(n):
        if d in digits:
            return True
        digits.add(d)
    return False

def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.readline().strip())
    
    count = 0
    num = 0
    
    while count < N:
        num += 1
        if not has_duplicate_digits(num):
            count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(num))

if __name__ == '__main__':
    main()
