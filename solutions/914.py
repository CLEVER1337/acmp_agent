
def read_parallelepiped():
    vertex = list(map(int, input().split()))
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    v3 = list(map(int, input().split()))
    
    points = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                x = vertex[0] + i * v1[0] + j * v2[0] + k * v3[0]
                y = vertex[1] + i * v1[1] + j * v2[1] + k * v3[1]
                z = vertex[2] + i * v1[2] + j * v2[2] + k * v3[2]
                points.append((x, y, z))
    
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    min_z = min(p[2] for p in points)
    max_z = max(p[2] for p in points)
    
    return (min_x, max_x, min_y, max_y, min_z, max_z)

def intersect(a, b):
    a_min_x, a_max_x, a_min_y, a_max_y, a_min_z, a_max_z = a
    b_min_x, b_max_x, b_min_y, b_max_y, b_min_z, b_max_z = b
    
    if (a_max_x < b_min_x or b_max_x < a_min_x or
        a_max_y < b_min_y or b_max_y < a_min_y or
        a_max_z < b_min_z or b_max_z < a_min_z):
        return False
    return True

def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines if line.strip()]
    
    p1_vertex = list(map(int, lines[0].split()))
    p1_v1 = list(map(int, lines[1].split()))
    p1_v2 = list(map(int, lines[2].split()))
    p1_v3 = list(map(int, lines[3].split()))
    
    p2_vertex = list(map(int, lines[4].split()))
    p2_v1 = list(map(int, lines[5].split()))
    p2_v2 = list(map(int, lines[6].split()))
    p2_v3 = list(map(int, lines[7].split()))
    
    def get_bounds(vertex, v1, v2, v3):
        points = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    x = vertex[0] + i * v1[0] + j * v2[0] + k * v3[0]
                    y = vertex[1] + i * v1[1] + j * v2[1] + k * v3[1]
                    z = vertex[2] + i * v1[2] + j * v2[2] + k * v3[2]
                    points.append((x, y, z))
        
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)
        min_z = min(p[2] for p in points)
        max_z = max(p[2] for p in points)
        
        return (min_x, max_x, min_y, max_y, min_z, max_z)
    
    bounds1 = get_bounds(p1_vertex, p1_v1, p1_v2, p1_v3)
    bounds2 = get_bounds(p2_vertex, p2_v1, p2_v2, p2_v3)
    
    if intersect(bounds1, bounds2):
        result = "YES"
    else:
        result = "NO"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
