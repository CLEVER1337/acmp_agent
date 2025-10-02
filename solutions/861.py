
def main():
    N = int(input().strip())
    result = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            d1 = i
            d2 = N // i
            result += d1 * (N // d1 - 1)
            if d1 != d2:
                result += d2 * (N // d2 - 1)
        i += 1
    print(result)

if __name__ == '__main__':
    main()
