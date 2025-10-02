
import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        k = int(data[index])
        p = int(data[index + 1])
        index += 2
        
        if p == 1:
            if k == 1:
                results.append("1")
            else:
                results.append("No solution")
            continue
            
        if k == 1:
            results.append("1")
            continue
            
        if k == 2:
            results.append(str(p))
            continue
            
        if k == 3:
            results.append(str(p - 1))
            continue
            
        if k <= p:
            results.append(str(p - k + 2))
            continue
            
        if k > 2 * p - 2:
            results.append("No solution")
            continue
            
        results.append(str(k - p + 1))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
