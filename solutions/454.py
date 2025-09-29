
def main():
    with open('INPUT.TXT', 'r') as f:
        M = int(f.readline().strip())
        N = int(f.readline().strip())
    
    n = N - M + 1
    result = M - 1
    
    while n > 1:
        if n % 2 == 1:
            result += (n + 1) // 2
        n //= 2
    
    result += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
