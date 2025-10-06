
def main():
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        print(0)
        return
        
    if n % 2 != 0:
        print(-1)
        return
        
    count = 0
    while n > 0 or m > 0:
        if m % 2 != 0:
            m += 1
            count += 1
        elif n > 0:
            n -= 2
            count += 1
        else:
            m -= 2
            count += 1
            
        if count > 100000:
            print(-1)
            return
            
    print(count)

if __name__ == "__main__":
    main()
