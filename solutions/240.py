
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n = int(data[0].strip())
    views = []
    index = 1
    for _ in range(6):
        view = []
        for i in range(n):
            line = data[index].strip()
            index += 1
            view.append(line)
        views.append(view)
    
    front = views[0]
    left = views[1]
    back = views[2]
    right = views[3]
    top = views[4]
    bottom = views[5]
    
    cube = [[[True for _ in range(n)] for _ in range(n)] for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if front[z][x] == '.':
                    if cube[x][y][z]:
                        cube[x][y][z] = False
                if left[z][y] == '.':
                    if cube[x][y][z]:
                        cube[x][y][z] = False
                if back[z][n-1-x] == '.':
                    if cube[x][y][z]:
                        cube[x][y][z] = False
                if right[z][n-1-y] == '.':
                    if cube[x][y][z]:
                        cube[x][y][z] = False
                if top[n-1-y][x] == '.':
                    if cube[x][y][z]:
                        cube[x][y][z] = False
                if bottom[y][x] == '.':
                    if cube[x][y][z]:
                        cube[x][y][z] = False
    
    for x in range(n):
        for z in range(n):
            color = front[z][x]
            if color != '.':
                found = False
                for y in range(n):
                    if cube[x][y][z] and (front[z][x] == color or front[z][x] != '.'):
                        found = True
                        break
                if not found:
                    for y in range(n):
                        if cube[x][y][z]:
                            cube[x][y][z] = False
    
    for y in range(n):
        for z in range(n):
            color = left[z][y]
            if color != '.':
                found = False
                for x in range(n):
                    if cube[x][y][z] and (left[z][y] == color or left[z][y] != '.'):
                        found = True
                        break
                if not found:
                    for x in range(n):
                        if cube[x][y][z]:
                            cube[x][y][z] = False
    
    for x in range(n):
        for z in range(n):
            color = back[z][n-1-x]
            if color != '.':
                found = False
                for y in range(n):
                    if cube[x][y][z] and (back[z][n-1-x] == color or back[z][n-1-x] != '.'):
                        found = True
                        break
                if not found:
                    for y in range(n):
                        if cube[x][y][z]:
                            cube[x][y][z] = False
    
    for y in range(n):
        for z in range(n):
            color = right[z][n-1-y]
            if color != '.':
                found = False
                for x in range(n):
                    if cube[x][y][z] and (right[z][n-1-y] == color or right[z][n-1-y] != '.'):
                        found = True
                        break
                if not found:
                    for x in range(n):
                        if cube[x][y][z]:
                            cube[x][y][z] = False
    
    for x in range(n):
        for y in range(n):
            color = top[n-1-y][x]
            if color != '.':
                found = False
                for z in range(n):
                    if cube[x][y][z] and (top[n-1-y][x] == color or top[n-1-y][x] != '.'):
                        found = True
                        break
                if not found:
                    for z in range(n):
                        if cube[x][y][z]:
                            cube[x][y][z] = False
    
    for x in range(n):
        for y in range(n):
            color = bottom[y][x]
            if color != '.':
                found = False
                for z in range(n):
                    if cube[x][y][z] and (bottom[y][x] == color or bottom[y][x] != '.'):
                        found = True
                        break
                if not found:
                    for z in range(n):
                        if cube[x][y][z]:
                            cube[x][y][z] = False
    
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if cube[x][y][z]:
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    main()
