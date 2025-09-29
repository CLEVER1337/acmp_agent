
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
        elif m < n - 1:
            results.append("No")
        elif m == n * (n - 1) // 2:
            results.append("Yes")
        else:
            max_edges = n * (n - 1) // 2
            if m > max_edges - (n - 1):
                results.append("No")
            else:
                results.append("Yes")
                
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
