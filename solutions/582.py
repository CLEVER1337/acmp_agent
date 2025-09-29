
def main():
    with open('INPUT.TXT', 'r') as f:
        cube1 = list(map(int, f.readline().split()))
        cube2 = list(map(int, f.readline().split()))
    
    def generate_rotations(cube):
        rotations = []
        # Исходная ориентация
        rotations.append(cube)
        
        # Повороты вокруг вертикальной оси
        for _ in range(3):
            cube = [cube[0], cube[1], cube[2], cube[3], cube[5], cube[4]]
            rotations.append(cube)
        
        # Повороты вокруг горизонтальной оси (вперед-назад)
        cube_rot = [cube[2], cube[3], cube[1], cube[0], cube[4], cube[5]]
        rotations.append(cube_rot)
        for _ in range(3):
            cube_rot = [cube_rot[0], cube_rot[1], cube_rot[2], cube_rot[3], cube_rot[5], cube_rot[4]]
            rotations.append(cube_rot)
        
        # Повороты вокруг оси лево-право
        cube_rot = [cube[4], cube[5], cube[2], cube[3], cube[1], cube[0]]
        rotations.append(cube_rot)
        for _ in range(3):
            cube_rot = [cube_rot[0], cube_rot[1], cube_rot[2], cube_rot[3], cube_rot[5], cube_rot[4]]
            rotations.append(cube_rot)
        
        return rotations
    
    rotations1 = generate_rotations(cube1)
    
    for rot in rotations1:
        if rot == cube2:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('YES')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('NO')

if __name__ == '__main__':
    main()
