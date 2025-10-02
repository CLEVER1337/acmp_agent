
def main():
    with open('INPUT.TXT', 'r') as f:
        cube1 = list(map(int, f.readline().split()))
        cube2 = list(map(int, f.readline().split()))
    
    def generate_rotations(cube):
        rotations = []
        # Основные вращения вокруг осей
        # Вращения вокруг вертикальной оси (верх-низ)
        def rotate_y(c):
            return [c[2], c[3], c[1], c[0], c[4], c[5]]
        
        # Вращения вокруг горизонтальной оси (лево-право)
        def rotate_x(c):
            return [c[4], c[5], c[2], c[3], c[1], c[0]]
        
        # Вращения вокруг передне-задней оси
        def rotate_z(c):
            return [c[0], c[1], c[5], c[4], c[2], c[3]]
        
        # Генерируем все возможные ориентации
        for _ in range(4):
            for _ in range(4):
                rotations.append(tuple(cube))
                cube = rotate_z(cube)
            cube = rotate_x(cube)
        
        cube = rotate_y(cube)
        for _ in range(4):
            rotations.append(tuple(cube))
            cube = rotate_z(cube)
        
        cube = rotate_y(cube)
        cube = rotate_y(cube)
        for _ in range(4):
            rotations.append(tuple(cube))
            cube = rotate_z(cube)
        
        return set(rotations)
    
    rotations1 = generate_rotations(cube1)
    
    with open('OUTPUT.TXT', 'w') as f:
        if tuple(cube2) in rotations1:
            f.write('YES')
        else:
            f.write('NO')

if __name__ == '__main__':
    main()
