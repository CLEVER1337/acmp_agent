
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].strip()
    
    result = [0] * n
    l = 0
    r = -1
    z = [0] * n
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        result[i] = z[i]
    
    result[0] = 1
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
