
def main():
    N = int(input().strip())
    count = 0
    num = 1
    while count < N:
        s = str(num)
        total = sum(int(d) for d in s)
        if total % len(s) == 0:
            count += 1
            if count == N:
                print(num)
                return
        num += 1

if __name__ == '__main__':
    main()
