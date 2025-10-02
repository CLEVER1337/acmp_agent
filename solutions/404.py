
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    if N == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('LOSE')
        return
    
    sqrt_n = int(math.isqrt(N))
    if sqrt_n * sqrt_n == N:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('LOSE')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('WIN')

if __name__ == '__main__':
    main()
