
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    idx = 0
    Nb, Mb = map(int, data[idx].split())
    idx += 1
    
    base = []
    for i in range(Nb):
        base.append(data[idx].strip())
        idx += 1
    
    Nd, Md = map(int, data[idx].split())
    idx += 1
    
    desert = []
    for i in range(Nd):
        desert.append(data[idx].strip())
        idx += 1
    
    def matches(desert_i, desert_j):
        for i in range(Nb):
            for j in range(Mb):
                di = desert_i + i
                dj = desert_j + j
                if di >= Nd or dj >= Md:
                    return False
                if base[i][j] == '#' and desert[di][dj] != '#':
                    return False
        return True
    
    count = 0
    for i in range(Nd - Nb + 1):
        for j in range(Md - Mb + 1):
            if matches(i, j):
                count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
