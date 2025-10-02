
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    index = 1
    results = []
    for _ in range(n):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        
        total = A + B + C
        max_val = max(A, B, C)
        
        if max_val > total - max_val + 1:
            results.append("No")
        else:
            results.append("Yes")
            
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
