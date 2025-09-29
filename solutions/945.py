
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    scores = list(map(int, data[2:2+n]))
    queries = list(map(int, data[2+n:2+n+k]))
    
    results = []
    for query in queries:
        left, right = 0, n - 1
        found = False
        while left <= right:
            mid = (left + right) // 2
            if scores[mid] == query:
                found = True
                break
            elif scores[mid] < query:
                left = mid + 1
            else:
                right = mid - 1
                
        results.append("YES" if found else "NO")
    
    sys.stdout.write(" ".join(results))

if __name__ == "__main__":
    main()
