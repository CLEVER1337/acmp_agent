
def main():
    with open('INPUT.TXT', 'r') as f:
        text = f.read().strip()
    
    n = len(text)
    fib_chars = []
    a, b = 1, 1
    
    while a <= n:
        fib_chars.append(text[a-1])
        a, b = b, a + b
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(fib_chars))

if __name__ == '__main__':
    main()
