
def extended_gcd(a, b):
    steps = []
    while b != 0:
        steps.append((a, b))
        a, b = b, a % b
    steps.append((a, 0))
    return steps

def solve():
    import sys
    data = sys.stdin.read().split()
    k = int(data[0])
    index = 1
    results = []
    
    for _ in range(k):
        a = int(data[index]); b = int(data[index+1]); index += 2
        c = int(data[index]); d = int(data[index+1]); index += 2
        
        if c == 0 or d == 0:
            if (a, b) == (c, d):
                results.append("YES")
            else:
                results.append("NO")
            continue
            
        if (c > a or d > b) and (c > b or d > a):
            results.append("NO")
            continue
            
        found = False
        current_a, current_b = a, b
        
        while current_b != 0:
            if (current_a, current_b) == (c, d):
                found = True
                break
            if current_a == c and current_b == d:
                found = True
                break
            if current_a < c or current_b < d:
                break
                
            if current_a >= current_b:
                if current_b > 0 and d == current_b:
                    n = (current_a - c) // current_b
                    if n >= 0 and current_a - n * current_b == c:
                        found = True
                        break
                current_a, current_b = current_b, current_a % current_b
            else:
                if current_a > 0 and c == current_a:
                    n = (current_b - d) // current_a
                    if n >= 0 and current_b - n * current_a == d:
                        found = True
                        break
                current_a, current_b = current_a, current_b % current_a
                
        if not found and (current_a, current_b) == (c, d):
            found = True
            
        results.append("YES" if found else "NO")
    
    for res in results:
        print(res)

solve()
