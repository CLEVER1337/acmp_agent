
def main():
    with open('INPUT.TXT', 'r') as f:
        text = f.readline().strip()
    
    n = len(text)
    fib_indices = []
    a, b = 1, 1
    
    while a <= n:
        fib_indices.append(a)
        a, b = b, a + b
    
    result = ''.join(text[i-1] for i in fib_indices if i <= n)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
