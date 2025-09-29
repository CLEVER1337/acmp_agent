
def read_input():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
        triangle = []
        for i in range(3):
            x, y = map(int, lines[i].split())
            triangle.append((x, y))
        x4, y4 = map(int, lines[3].split())
        return triangle, (x4, y4)

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_in_triangle(triangle, point):
    v1, v2, v3 = triangle
    d1 = sign(point, v1, v2)
    d2 = sign(point, v2, v3)
    d3 = sign(point, v3, v1)
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)

def main():
    triangle, point = read_input()
    result = "In" if point_in_triangle(triangle, point) else "Out"
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
