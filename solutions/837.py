
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
        
        if n == 1:
            if m == 0:
                results.append("Yes")
            else:
                results.append("No")
        else:
            max_edges = n * (n - 1) // 2
            if m > max_edges:
                results.append("No")
            elif m < n - 1:
                results.append("No")
            else:
                results.append("Yes")
                
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
