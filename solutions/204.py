
def main():
    s = input().strip()
    n = len(s)
    prefix = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        else:
            j = 0
        prefix[i] = j
    
    candidate = n - prefix[-1]
    if n % candidate == 0:
        print(candidate)
    else:
        print(n)

if __name__ == "__main__":
    main()
