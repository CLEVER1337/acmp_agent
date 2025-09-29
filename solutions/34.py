
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    if k > n:
        print("NO")
        return
        
    patterns = set()
    for i in range(n - k + 1):
        pattern = s[i:i+k]
        if pattern in patterns:
            print("YES")
            return
        patterns.add(pattern)
        
    print("NO")

if __name__ == "__main__":
    main()
