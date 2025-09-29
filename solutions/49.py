
def main():
    with open('INPUT.TXT', 'r') as f:
        p1 = f.readline().strip()
        p2 = f.readline().strip()
    
    n = len(p1)
    count = 1
    
    for i in range(n):
        c1, c2 = p1[i], p2[i]
        
        if c1 == '?' and c2 == '?':
            count *= 10
        elif c1 == '?':
            if c2 in '0123456789':
                count *= 1
            else:
                count *= 7
        elif c2 == '?':
            if c1 in '0123456789':
                count *= 1
            else:
                count *= 7
        else:
            if c1 in '0123456789' and c2 in '0123456789':
                if c1 != c2:
                    count = 0
                    break
            elif c1 in '0123456789':
                if c1 != '0' and c2 == 'a':
                    count *= 1
                elif c1 != '1' and c2 == 'b':
                    count *= 1
                elif c1 != '2' and c2 == 'c':
                    count *= 1
                elif c1 != '3' and c2 == 'd':
                    count *= 1
                elif c1 != '4' and c2 == 'e':
                    count *= 1
                elif c1 != '5' and c2 == 'f':
                    count *= 1
                elif c1 != '6' and c2 == 'g':
                    count *= 1
                else:
                    count = 0
                    break
            elif c2 in '0123456789':
                if c2 != '0' and c1 == 'a':
                    count *= 1
                elif c2 != '1' and c1 == 'b':
                    count *= 1
                elif c2 != '2' and c1 == 'c':
                    count *= 1
                elif c2 != '3' and c1 == 'd':
                    count *= 1
                elif c2 != '4' and c1 == 'e':
                    count *= 1
                elif c2 != '5' and c1 == 'f':
                    count *= 1
                elif c2 != '6' and c1 == 'g':
                    count *= 1
                else:
                    count = 0
                    break
            else:
                if c1 != c2:
                    count = 0
                    break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
