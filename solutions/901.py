
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n == 1:
        result = 0
    else:
        result = 1
        a, b = 1, 1
        while True:
            a, b = b, a + b
            if b > n:
                break
            result += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
