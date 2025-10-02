
import sys

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    index = 1
    results = []
    for _ in range(k):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        if m > n * (n - 1) // 2:
            results.append("No")
            continue
            
        if n == 1:
            if m == 0:
                results.append("Yes")
            else:
                results.append("No")
            continue
            
        min_edges = n - 1
        if m < min_edges:
            results.append("No")
            continue
            
        max_edges_planar = 3 * n - 6
        if m <= max_edges_planar:
            results.append("Yes")
        else:
            results.append("No")
            
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
