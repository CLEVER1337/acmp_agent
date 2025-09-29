
def main():
    n = int(input().strip())
    if n <= 4:
        print(n)
        return
        
    result = 1
    while n > 4:
        result *= 3
        n -= 3
    result *= n
    print(result)

if __name__ == "__main__":
    main()
