
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.read().split())
    
    g = math.gcd(n, m)
    result = n // g
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
