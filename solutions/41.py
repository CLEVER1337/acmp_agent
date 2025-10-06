
def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()
