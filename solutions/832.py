
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    index = 1
    results = []
    for _ in range(n):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        
        total = a + b + c
        if total == 0:
            results.append("No")
            continue
            
        max_val = max(a, b, c)
        if max_val > total - max_val + 1:
            results.append("No")
        else:
            results.append("Yes")
            
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
