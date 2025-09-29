
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.readline().strip())
    
    if N == 0:
        result = 10
    elif N < 10:
        result = N
    else:
        factors = []
        for digit in range(9, 1, -1):
            while N % digit == 0:
                factors.append(str(digit))
                N //= digit
        
        if N != 1:
            result = -1
        else:
            factors.sort()
            result = ''.join(factors)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
