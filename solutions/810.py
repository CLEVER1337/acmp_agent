
def main():
    import sys
    data = sys.stdin.readline().split()
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])
    
    n0 = a * c + 1
    n = n0
    
    def check(n_val):
        min_u = max(a, (n_val + d - 1) // d)
        max_u = min(b, n_val // c)
        if min_u > max_u:
            return True
        for u in range(min_u, max_u + 1):
            if n_val % u == 0:
                v = n_val // u
                if c <= v <= d:
                    return False
        return True
    
    while True:
        if check(n):
            print(n)
            return
        n += 1

if __name__ == "__main__":
    main()
