
def main():
    p1 = input().strip()
    p2 = input().strip()
    n = len(p1)
    count = 1
    for i in range(n):
        c1 = p1[i]
        c2 = p2[i]
        if c1 == '?' and c2 == '?':
            count *= 10
        elif c1 == '?' and c2 != '?':
            if c2 in 'abcdefg':
                count *= 7
            else:
                count *= 1
        elif c1 != '?' and c2 == '?':
            if c1 in 'abcdefg':
                count *= 7
            else:
                count *= 1
        else:
            if c1 == c2:
                count *= 1
            elif c1 in 'abcdefg' and c2 in 'abcdefg':
                count *= 0
            elif c1 in 'abcdefg' and c2 in '0123456789':
                if int(c2) < 7:
                    count *= 0
                else:
                    count *= 1
            elif c1 in '0123456789' and c2 in 'abcdefg':
                if int(c1) < 7:
                    count *= 0
                else:
                    count *= 1
            else:
                count *= 0
    print(count)

if __name__ == '__main__':
    main()
