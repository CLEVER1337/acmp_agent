
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lattice_points_on_segment(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    g = gcd(dx, dy)
    return g - 1

def area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def main():
    data = list(map(int, input().split()))
    x1, y1, x2, y2, x3, y3 = data
    
    b1 = lattice_points_on_segment(x1, y1, x2, y2) + 1
    b2 = lattice_points_on_segment(x2, y2, x3, y3) + 1
    b3 = lattice_points_on_segment(x3, y3, x1, y1) + 1
    
    total_boundary = b1 + b2 + b3 - 3
    
    A = area(x1, y1, x2, y2, x3, y3)
    
    I = (A - total_boundary) // 2 + 1
    
    result = total_boundary + I
    print(result)

if __name__ == "__main__":
    main()
