
def main():
    s = input().strip()
    n = len(s)
    distinct_substrings = set()
    for i in range(n):
        for j in range(i, n):
            distinct_substrings.add(s[i:j+1])
    print(len(distinct_substrings))

if __name__ == "__main__":
    main()
