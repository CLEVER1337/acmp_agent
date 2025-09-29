
def main():
    with open('INPUT.TXT', 'r') as f:
        m, n, x, y = map(int, f.read().split())
    
    if (m + n) % 2 != (x + y) % 2:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    if m == x and n == y:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    dx = x - m
    dy = y - n
    
    if abs(dx) == abs(dy):
        with open('OUTPUT.TXT', 'w') as f:
            f.write('1')
        return
    
    found = False
    for i in range(1, 9):
        for j in range(1, 9):
            if abs(m - i) == abs(n - j) and abs(x - i) == abs(y - j):
                found = True
                intermediate = (i, j)
                break
        if found:
            break
    
    if found:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('2\n')
            f.write(f'{intermediate[0]} {intermediate[1]}')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')

if __name__ == '__main__':
    main()
