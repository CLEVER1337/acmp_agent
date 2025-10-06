
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    if n == 1 and m == 1:
        print(4)
    else:
        result = n * m * 2 + 2
        if n == 1 or m == 1:
            result += abs(n - m) * 2
        print(result)

if __name__ == "__main__":
    main()
