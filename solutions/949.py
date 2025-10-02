
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        n = int(data[0])
        a_n = int(data[1])
        a_n1 = int(data[2])
    
    if n == 1:
        a1 = a_n
        a2 = a_n1
    elif n == 2:
        a1 = a_n
        a2 = a_n1
    else:
        fib = [0] * (n + 2)
        fib[n] = a_n
        fib[n + 1] = a_n1
        
        for i in range(n - 1, 0, -1):
            fib[i] = fib[i + 2] - fib[i + 1]
        
        a1 = fib[1]
        a2 = fib[2]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{a1} {a2}")

if __name__ == "__main__":
    main()
