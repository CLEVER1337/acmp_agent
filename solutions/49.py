
def main():
    with open('INPUT.TXT', 'r') as f:
        p1 = f.readline().strip()
        p2 = f.readline().strip()
    
    n = len(p1)
    count = 1
    
    for i in range(n):
        c1, c2 = p1[i], p2[i]
        
        if c1 == '?' and c2 == '?':
            count *= 16
        elif c1 == '?':
            if c2 in '0123456789abcdefg':
                count *= 1
            else:
                count *= 0
        elif c2 == '?':
            if c1 in '0123456789abcdefg':
                count *= 1
            else:
                count *= 0
        else:
            if c1 == c2 and c1 in '0123456789abcdefg':
                count *= 1
            else:
                count *= 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
