
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.read().split())
    
    if n == 1 and m == 1:
        result = 4
    else:
        result = n * m * 2 + n + m
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
