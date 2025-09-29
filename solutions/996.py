
def main():
    n = int(input().strip())
    if n == 1:
        print(1)
        return
    
    a = [0] * (n + 1)
    seen = set()
    a[1] = 1
    seen.add(1)
    
    for i in range(2, n + 1):
        if i in seen:
            a[i] = a[i - 1] + 3
        else:
            a[i] = a[i - 1] + 2
        seen.add(a[i])
    
    print(a[n])

if __name__ == "__main__":
    main()
