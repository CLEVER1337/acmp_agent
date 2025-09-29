
with open('INPUT.TXT', 'r') as f:
    data = f.read().splitlines()

w, h = map(int, data[0].split())
img1 = []
for i in range(1, 1+h):
    img1.append(data[i].strip())

img2 = []
for i in range(1+h, 1+2*h):
    img2.append(data[i].strip())

op = list(map(int, data[1+2*h].split()))

result = []
for y in range(h):
    row = ''
    for x in range(w):
        p1 = int(img1[y][x])
        p2 = int(img2[y][x])
        
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
