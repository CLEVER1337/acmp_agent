
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].strip()
    
    res = [0] * n
    res[0] = 1
    
    l, r = 0, 0
    z = [0] * n
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    t = s[::-1]
    s_rev = t
    z_rev = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z_rev[i] = min(r - i + 1, z_rev[i - l])
        while i + z_rev[i] < n and s_rev[z_rev[i]] == s_rev[i + z_rev[i]]:
            z_rev[i] += 1
        if i + z_rev[i] - 1 > r:
            l = i
            r = i + z_rev[i] - 1
            
    for i in range(n):
        j = n - i - 1
        if z_rev[j] >= i + 1:
            res[i] = i + 1
        else:
            res[i] = z_rev[j]
            
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
