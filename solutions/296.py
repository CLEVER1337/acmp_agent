
def main():
    n = int(input().strip())
    for x in range(n // 5, -1, -1):
        remainder = n - x * 5
        if remainder % 3 == 0:
            y = remainder // 3
            print(f"{x} {y}")
            return
    print("0 0")

if __name__ == "__main__":
    main()
