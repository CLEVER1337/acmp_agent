
def read_input():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    n1, m1 = map(int, data[0].split())
    grid1 = data[1:1+n1]
    
    n2, m2 = map(int, data[1+n1].split())
    grid2 = data[2+n1:2+n1+n2]
    
    return grid1, grid2

def rotate_90(grid):
    return [''.join(row[i] for row in grid[::-1]) for i in range(len(grid[0]))]

def reflect_vertical(grid):
    return [row[::-1] for row in grid]

def generate_all_transformations(grid):
    transformations = []
    current = grid
    
    for _ in range(4):
        transformations.append(current)
        transformations.append(reflect_vertical(current))
        current = rotate_90(current)
    
    return transformations

def are_grids_equal(grid1, grid2):
    return grid1 == grid2

def solve():
    grid1, grid2 = read_input()
    
    if len(grid1) != len(grid2) or len(grid1[0]) != len(grid2[0]):
        transformations = generate_all_transformations(grid1)
        for transformed in transformations:
            if len(transformed) == len(grid2) and len(transformed[0]) == len(grid2[0]):
                if transformed == grid2:
                    with open('OUTPUT.TXT', 'w') as f:
                        f.write('Yes')
                    return
    else:
        transformations = generate_all_transformations(grid1)
        for transformed in transformations:
            if transformed == grid2:
                with open('OUTPUT.TXT', 'w') as f:
                    f.write('Yes')
                return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('No')

if __name__ == '__main__':
    solve()
