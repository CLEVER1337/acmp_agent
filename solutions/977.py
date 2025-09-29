
def main():
    n = int(input().strip())
    if n == 2:
        print(1)
    else:
        result = pow(2, (n-1)*(n-2)//2) - 1
        result = pow(result, 1, 10**9+7) if result >= 0 else result
        print(result % (10**9+7))

if __name__ == "__main__":
    main()
