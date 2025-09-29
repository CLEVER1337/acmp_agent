
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n == 1:
        result = [(0, 0)]
    elif n == 2 or n == 3:
        result = None
    else:
        result = []
        if n % 6 == 2:
            for i in range(2, n+1, 2):
                result.append((i-1, i-1))
            result.append((2-1, 0))
            result.append((0, 3-1))
            for i in range(7, n+1):
                if i % 2 == 1:
                    result.append((i-1, i-3))
                else:
                    result.append((i-1, i+1))
            if n > 4:
                result.append((5-1, 1))
        elif n % 6 == 3:
            for i in range(4, n+1, 2):
                result.append((i-1, i-1))
            result.append((2-1, 0))
            result.append((0, 1))
            result.append((3-1, 2))
            for i in range(7, n+1):
                if i % 2 == 1:
                    result.append((i-1, i-3))
                else:
                    result.append((i-1, i+1))
            if n > 4:
                result.append((5-1, 3))
        else:
            for i in range(1, n+1):
                if i % 2 == 0:
                    result.append((i-1, n//2 + i//2 - 1))
                else:
                    result.append((i-1, i//2))
    
    with open('OUTPUT.TXT', 'w') as f:
        if result is None:
            f.write('No solution')
        else:
            for row, col in result:
                f.write(f'{row} {col}\n')

if __name__ == '__main__':
    main()
