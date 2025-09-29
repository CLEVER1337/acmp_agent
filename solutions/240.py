
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
            view.append(data[index].strip())
            index += 1
            if i < n - 1 and index < len(data) and data[index].strip() == '':
                index += 1
        views.append(view)
    
    front, left, back, right, top, bottom = views
    
    cube = [[[True for _ in range(n)] for _ in range(n)] for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if front[z][x] == '.':
                    cube[x][y][n-1-z] = False
                if back[z][n-1-x] == '.':
                    cube[x][y][z] = False
                if left[z][y] == '.':
                    cube[n-1-y][x][z] = False
                if right[z][n-1-y] == '.':
                    cube[y][x][z] = False
                if top[y][x] == '.':
                    cube[x][n-1-y][n-1-z] = False
                if bottom[n-1-y][x] == '.':
                    cube[x][y][z] = False
    
    for i in range(n):
        for j in range(n):
            if front[i][j] != '.':
                found = False
                for k in range(n):
                    if cube[j][k][n-1-i]:
                        found = True
                        break
                if not found:
                    for k in range(n):
                        cube[j][k][n-1-i] = False
            
            if left[i][j] != '.':
                found = False
                for k in range(n):
                    if cube[n-1-j][k][i]:
                        found = True
                        break
                if not found:
                    for k in range(n):
                        cube[n-1-j][k][i] = False
            
            if back[i][j] != '.':
                found = False
                for k in range(n):
                    if cube[n-1-j][k][n-1-i]:
                        found = True
                        break
                if not found:
                    for k in range(n):
                        cube[n-1-j][k][n-1-i] = False
            
            if right[i][j] != '.':
                found = False
                for k in range(n):
                    if cube[j][k][n-1-i]:
                        found = True
                        break
                if not found:
                    for k in range(n):
                        cube[j][k][n-1-i] = False
            
            if top[i][j] != '.':
                found = False
                for k in range(n):
                    if cube[j][i][k]:
                        found = True
                        break
                if not found:
                    for k in range(n):
                        cube[j][i][k] = False
            
            if bottom[i][j] != '.':
                found = False
                for k in range(n):
                    if cube[j][n-1-i][k]:
                        found = True
                        break
                if not found:
                    for k in range(n):
                        cube[j][n-1-i][k] = False
    
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if cube[x][y][z]:
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    main()
