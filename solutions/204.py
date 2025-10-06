
def main():
    s = input().strip()
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        else:
            j = 0
        pi[i] = j
    
    k = n - pi[n - 1]
    if n % k == 0:
        print(k)
    else:
        print(n)

if __name__ == "__main__":
    main()
