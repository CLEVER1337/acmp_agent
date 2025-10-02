
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    if n % 2 == 0:
        a = n // 2
        b = n // 2
    else:
        if n % 3 == 0:
            a = n // 3
            b = 2 * n // 3
        else:
            a = 1
            b = n - 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{a} {b}")

if __name__ == "__main__":
    main()
