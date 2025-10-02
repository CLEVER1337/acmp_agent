
def read_parallelepiped():
    vertex = list(map(int, input().split()))
    edges = []
    for _ in range(3):
        edges.append(list(map(int, input().split())))
    return vertex, edges

def get_all_vertices(vertex, edges):
    vertices = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                v = [
                    vertex[0] + i * edges[0][0] + j * edges[1][0] + k * edges[2][0],
                    vertex[1] + i * edges[0][1] + j * edges[1][1] + k * edges[2][1],
                    vertex[2] + i * edges[0][2] + j * edges[1][2] + k * edges[2][2]
                ]
                vertices.append(v)
    return vertices

def get_projection_range(vertices, axis):
    coords = [v[axis] for v in vertices]
    return min(coords), max(coords)

def check_intersection_1d(range1, range2):
    return not (range1[1] < range2[0] or range2[1] < range1[0])

def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    vertex1 = list(map(int, lines[0].split()))
    edges1 = [list(map(int, line.split())) for line in lines[1:4]]
    
    vertex2 = list(map(int, lines[4].split()))
    edges2 = [list(map(int, line.split())) for line in lines[5:8]]
    
    vertices1 = get_all_vertices(vertex1, edges1)
    vertices2 = get_all_vertices(vertex2, edges2)
    
    for axis in range(3):
        range1 = get_projection_range(vertices1, axis)
        range2 = get_projection_range(vertices2, axis)
        if not check_intersection_1d(range1, range2):
            with open('OUTPUT.TXT', 'w') as f:
                f.write('NO')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('YES')

if __name__ == "__main__":
    main()
