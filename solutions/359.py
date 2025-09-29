
def main():
    n = int(input().strip())
    if n == 1:
        print(1)
        return
        
    a, b = 1, 2
    for i in range(3, n+1):
        if i % 2 == 1:
            a = a + 4 * (i - 2) + 1
        else:
            b = b + 4 * (i - 2) + 1
            
    if n % 2 == 1:
        print(a)
    else:
        print(b)

if __name__ == "__main__":
    main()
