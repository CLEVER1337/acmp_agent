
import sys

def main():
    data = sys.stdin.read().split()
    index = 0
    results = []
    while index < len(data):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        if a == 0 and b == 0 and c == 0:
            break
        stones = sorted([a, b, c])
        x, y, z = stones
        if (x ^ y ^ z) == 0:
            results.append("Bob")
        else:
            results.append("Alice")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
