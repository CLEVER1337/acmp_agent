
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    total = 0
    for i in range(n):
        diff = 0
        left = i
        right = i
        while left >= 0 and right < n:
            if s[left] != s[right]:
                diff += 1
            if diff <= k:
                total += 1
            else:
                break
            left -= 1
            right += 1
            
    for i in range(n - 1):
        diff = 0
        left = i
        right = i + 1
        while left >= 0 and right < n:
            if s[left] != s[right]:
                diff += 1
            if diff <= k:
                total += 1
            else:
                break
            left -= 1
            right += 1
            
    print(total)

if __name__ == "__main__":
    main()
