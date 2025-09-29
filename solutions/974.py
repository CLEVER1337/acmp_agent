
import sys

def main():
    data = sys.stdin.read().splitlines()
    results = []
    for line in data:
        a, b, c = map(int, line.split())
        if a == 0 and b == 0 and c == 0:
            break
            
        stones = sorted([a, b, c])
        x, y, z = stones
        
        if (x ^ y) == z:
            results.append("Bob")
        else:
            results.append("Alice")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
