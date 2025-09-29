
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def count_lattice_points_on_segment(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return gcd(dx, dy) + 1

def count_lattice_points_in_triangle(x1, y1, x2, y2, x3, y3):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    
    def boundary_points(x1, y1, x2, y2, x3, y3):
        b1 = count_lattice_points_on_segment(x1, y1, x2, y2) - 1
        b2 = count_lattice_points_on_segment(x2, y2, x3, y3) - 1
        b3 = count_lattice_points_on_segment(x3, y3, x1, y1) - 1
        return b1 + b2 + b3 + 3
    
    A = area(x1, y1, x2, y2, x3, y3)
    B = boundary_points(x1, y1, x2, y2, x3, y3)
    I = A - B/2 + 1
    
    return int(I)

def main():
    with open('INPUT.TXT', 'r') as f:
        data = list(map(int, f.read().split()))
    
    x1, y1, x2, y2, x3, y3 = data
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    def count_on_segment(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return gcd(dx, dy) + 1
    
    b1 = count_on_segment(x1, y1, x2, y2) - 1
    b2 = count_on_segment(x2, y2, x3, y3) - 1
    b3 = count_on_segment(x3, y3, x1, y1) - 1
    boundary_points = b1 + b2 + b3 + 3
    
    area2 = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    interior_points = (area2 - boundary_points + 2) // 2
    
    result = boundary_points + interior_points
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
