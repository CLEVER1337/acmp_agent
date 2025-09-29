
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        a, b, c = map(int, f.readline().split())
    
    if a == 0:
        if b == 0:
            if c == 0:
                with open('OUTPUT.TXT', 'w') as f:
                    f.write('-1')
                return
            else:
                with open('OUTPUT.TXT', 'w') as f:
                    f.write('0')
                return
        else:
            root = -c / b
            with open('OUTPUT.TXT', 'w') as f:
                f.write('1\n')
                f.write(f'{root:.6f}')
            return
    
    discriminant = b*b - 4*a*c
    
    if discriminant < 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
    elif discriminant == 0:
        root = -b / (2*a)
        with open('OUTPUT.TXT', 'w') as f:
            f.write('1\n')
            f.write(f'{root:.6f}')
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2*a)
        root2 = (-b + math.sqrt(discriminant)) / (2*a)
        if root1 > root2:
            root1, root2 = root2, root1
        with open('OUTPUT.TXT', 'w') as f:
            f.write('2\n')
            f.write(f'{root1:.6f}\n')
            f.write(f'{root2:.6f}')

if __name__ == '__main__':
    main()
