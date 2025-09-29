
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        a, b = map(int, f.read().split())
    
    area = a * b
    root = math.isqrt(area)
    
    if root * root == area:
        result = root
    else:
        result = 0
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
