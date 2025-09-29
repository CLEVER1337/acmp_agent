
def main():
    with open('INPUT.TXT', 'r') as f:
        F = int(f.readline().strip())
    
    n = 1
    while True:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        if factorial == F:
            break
        n += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(n))

if __name__ == '__main__':
    main()
