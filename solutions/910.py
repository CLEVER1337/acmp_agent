
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])
    
    total = 0
    fact = 1
    
    for k in range(1, N + 1):
        fact = (fact * k) % M
        term = (fact * 2 * k) % M
        total = (total + term) % M
        
    print(total)

if __name__ == "__main__":
    main()
