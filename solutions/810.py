
def main():
    import sys
    data = sys.stdin.readline().split()
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])
    
    n_start = a * c + 1
    
    def can_represent(n):
        min_u = max(a, (n + d - 1) // d)
        max_u = min(b, n // c)
        
        if min_u > max_u:
            return False
            
        for u in range(min_u, max_u + 1):
            if n % u == 0:
                v = n // u
                if c <= v <= d:
                    return True
        return False
    
    n = n_start
    while True:
        if not can_represent(n):
            print(n)
            return
        n += 1

if __name__ == "__main__":
    main()
