
def main():
    n = int(input().strip())
    count = 0
    num = 7
    while count < n:
        if bin(num).count('1') == 3:
            count += 1
            if count == n:
                break
        num += 1
    print(num)

if __name__ == "__main__":
    main()
