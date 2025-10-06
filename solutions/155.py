
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    target = float(data[1])
    caps = list(map(int, data[2:2+n]))
    
    def solve():
        from itertools import product
        
        if n == 0:
            return False
            
        all_schemes = [set() for _ in range(n+1)]
        for i in range(1, n+1):
            all_schemes[i].add(caps[i-1])
        
        for k in range(2, n+1):
            for a in range(1, k):
                b = k - a
                for ca in all_schemes[a]:
                    for cb in all_schemes[b]:
                        all_schemes[k].add(ca + cb)
                        all_schemes[k].add((ca * cb) / (ca + cb))
        
        for k in range(1, n+1):
            for cap in all_schemes[k]:
                if abs(cap - target) <= 0.01:
                    return True
        return False
    
    result = solve()
    print("YES" if result else "NO")

if __name__ == "__main__":
    main()
