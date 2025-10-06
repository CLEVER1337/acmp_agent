
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    w, h = map(int, data[0].split())
    img1 = []
    img2 = []
    
    index = 1
    for i in range(h):
        img1.append(data[index].strip())
        index += 1
        
    for i in range(h):
        img2.append(data[index].strip())
        index += 1
        
    op = list(map(int, data[index].split()))
    
    result = []
    for i in range(h):
        row = []
        for j in range(w):
            p1 = int(img1[i][j])
            p2 = int(img2[i][j])
            if p1 == 0 and p2 == 0:
                res = op[0]
            elif p1 == 0 and p2 == 1:
                res = op[1]
            elif p1 == 1 and p2 == 0:
                res = op[2]
            else:
                res = op[3]
            row.append(str(res))
        result.append(''.join(row))
    
    for line in result:
        print(line)

if __name__ == "__main__":
    main()
