
import sys

def main():
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
            
        left, right = 0, 10**20
        found = False
        while left <= right:
            mid = (left + right) // 2
            total = mid * p + 1
            if total == k:
                results.append(str(mid))
                found = True
                break
            elif total < k:
                left = mid + 1
            else:
                right = mid - 1
                
        if not found:
            results.append("No solution")
            
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
