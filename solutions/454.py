
def main():
    with open('INPUT.TXT', 'r') as f:
        M = int(f.readline().strip())
        N = int(f.readline().strip())
    
    length = N - M + 1
    step = 1
    start = M
    direction = 1
    
    while length > 1:
        if direction == 1:
            start = start + step
            length = (length - 1) // 2
            step *= 2
            direction = -1
        else:
            if length % 2 == 1:
                start = start + step
            length = length // 2
            step *= 2
            direction = 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(start))

if __name__ == '__main__':
    main()
