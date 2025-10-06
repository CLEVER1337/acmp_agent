
import sys

def main():
    data = sys.stdin.readline().split()
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])
    
    start = a * c + 1
    max_n = b * d + 1
    
    def has_factor(n):
        min_u = max(a, (n + d - 1) // d)
        max_u = min(b, n // c)
        if min_u <= max_u:
            return True
        return False
    
    n = start
    while n <= max_n:
        if not has_factor(n):
            print(n)
            return
        n += 1
        
    print(max_n)

if __name__ == "__main__":
    main()
