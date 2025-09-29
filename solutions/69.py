
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n, a = map(int, f.readline().split())
    
    r_out = a / (2 * math.sin(math.pi / n))
    r_in = a / (2 * math.tan(math.pi / n))
    quality = r_out - r_in
    
    if quality < 1:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('YES')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('NO')

if __name__ == '__main__':
    main()
