
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    blocks = []
    current_block = []
    for line in data:
        if line.strip():
            current_block.append(line)
        if len(current_block) == 4:
            blocks.append(current_block)
            current_block = []
    
    if len(current_block) == 4:
        blocks.append(current_block)
    
    cubes = []
    for block in blocks:
        base = list(map(int, block[0].split()))
        vectors = []
        for i in range(1, 4):
            vectors.append(list(map(int, block[i].split())))
        
        points = []
        for mask in range(8):
            point = base.copy()
            for i in range(3):
                if mask & (1 << i):
                    for j in range(3):
                        point[j] += vectors[i][j]
            points.append(point)
        
        min_coords = [min(p[i] for p in points) for i in range(3)]
        max_coords = [max(p[i] for p in points) for i in range(3)]
        cubes.append((min_coords, max_coords))
    
    cube1, cube2 = cubes
    
    intersect = True
    for i in range(3):
        if cube1[1][i] < cube2[0][i] or cube2[1][i] < cube1[0][i]:
            intersect = False
            break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('YES' if intersect else 'NO')

if __name__ == '__main__':
    main()
