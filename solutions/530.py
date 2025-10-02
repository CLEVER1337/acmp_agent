
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    w, h = map(int, data[0].split())
    img1 = data[1:1+h]
    img2 = data[1+h:1+2*h]
    op = list(map(int, data[1+2*h].split()))
    
    result = []
    for i in range(h):
        row = ''
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
            row += str(res)
        result.append(row)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    main()
