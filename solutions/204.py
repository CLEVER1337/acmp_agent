
def main():
    s = input().strip()
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    
    candidate = n - prefix[-1]
    if n % candidate == 0:
        print(candidate)
    else:
        print(n)

if __name__ == "__main__":
    main()
