
import sys

def main():
    data = sys.stdin.read().splitlines()
    results = []
    for line in data:
        a, b, c = map(int, line.split())
        if a == 0 and b == 0 and c == 0:
            break
        stones = sorted([a, b, c])
        if stones[0] ^ stones[1] == stones[2]:
            results.append("Bob")
        else:
            results.append("Alice")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
