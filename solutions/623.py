
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n == 0 or n == 1:
        result = 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, (a + b) % 10
        result = b
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
