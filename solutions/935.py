
def main():
    with open('INPUT.TXT', 'r') as f:
        x1, y1, x2, y2 = map(int, f.read().split())
    
    color1 = (x1 + y1) % 2
    color2 = (x2 + y2) % 2
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('YES' if color1 == color2 else 'NO')

if __name__ == '__main__':
    main()
