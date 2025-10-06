
import sys

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    index = 1
    results = []
    
    for _ in range(k):
        X = int(data[index])
        Y = int(data[index+1])
        A = int(data[index+2])
        index += 3
        
        perimeter = 2 * (X + Y) - 4
        if A == 1:
            results.append('1')
            continue
            
        if perimeter % A != 0:
            results.append('0')
            continue
            
        if A > max(X, Y):
            results.append('0')
            continue
            
        if X % A == 0 or Y % A == 0:
            results.append('1')
        else:
            results.append('0')
            
    print(''.join(results))

if __name__ == "__main__":
    main()
