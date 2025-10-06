
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    def mex(a, b):
        if a == 0 and b == 0:
            return 0
        if a == 0:
            return b
        if b == 0:
            return a
        x = min(a, b)
        y = max(a, b)
        if y % x == 0:
            return 0
        return mex(x, y % x)
    
    total = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            total += mex(i, j)
    
    print(total)

if __name__ == "__main__":
    main()
