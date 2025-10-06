
def main():
    n = int(input().strip())
    if n < 3:
        print(0)
        return
        
    count = 0
    while n > 3:
        if n % 2 == 0:
            count += n // 2
            n //= 2
        else:
            count += (n + 1) // 2
            n = (n - 1) // 2
            
    if n == 3:
        count += 1
        
    print(count)

if __name__ == "__main__":
    main()
