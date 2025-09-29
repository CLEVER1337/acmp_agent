
def main():
    s = input().strip()
    n = len(s)
    if n == 0:
        print(0)
        return
        
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    count = 0
    for i in range(n):
        if z[i] == n - i:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
