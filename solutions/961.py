
def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    n, m = map(int, data[0].split())
    grid1 = data[1:1+n]
    grid2 = data[2+n:2+2*n]
    
    pos1 = {}
    pos2 = {}
    
    for i in range(n):
        for j in range(m):
            char = grid1[i][j]
            if char != '.':
                pos1[char] = (i, j)
    
    for i in range(n):
        for j in range(m):
            char = grid2[i][j]
            if char != '.':
                pos2[char] = (i, j)
    
    moving = []
    for char in pos1:
        if pos1[char] != pos2[char]:
            moving.append(char)
    
    moving.sort(key=lambda x: (not x.islower(), x))
    
    print(len(moving))
    print(''.join(moving))

if __name__ == "__main__":
    main()
