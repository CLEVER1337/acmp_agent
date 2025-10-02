
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        F = int(f.readline().strip())
    
    n = 1
    while math.factorial(n) <= F:
        n += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(n - 1))

if __name__ == '__main__':
    main()
