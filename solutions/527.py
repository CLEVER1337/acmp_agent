
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    k = int(data[idx]); idx += 1
    results = []
    
    for _ in range(k):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        c = int(data[idx]); d = int(data[idx+1]); idx += 2
        
        if c > a or d > b:
            results.append("NO")
            continue
            
        found = False
        while b > 0:
            if a == c and b == d:
                found = True
                break
            if a < c or b < d:
                break
            if b > 0 and a >= b:
                if d > 0 and (a - c) % b == 0 and (a - c) // b >= 1 and b == d:
                    found = True
                    break
            a, b = b, a % b
            
        results.append("YES" if found else "NO")
    
    for res in results:
        print(res)

solve()
