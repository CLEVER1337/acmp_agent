
def main():
    s = input().strip()
    n = len(s)
    fibs = []
    a, b = 1, 1
    while a <= n:
        fibs.append(a)
        a, b = b, a + b
    
    result = ''.join(s[i-1] for i in fibs if i <= n)
    print(result)

if __name__ == "__main__":
    main()
