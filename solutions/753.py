
def main():
    s = input().strip()
    n = len(s)
    seen = set()
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            seen.add(substring)
    print(len(seen))

if __name__ == "__main__":
    main()
