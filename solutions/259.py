
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].strip()
    
    result = [0] * n
    result[0] = 1
    
    for i in range(1, n):
        k = result[i-1]
        if k > 0 and i - k >= 0 and s[i] == s[i - k]:
            result[i] = k + 1
        else:
            j = 0
            while j <= i and s[j] == s[i - j]:
                j += 1
            result[i] = j
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
