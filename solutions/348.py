
def cross_product(a, b):
    return a[0] * b[1] - a[1] * b[0]

def vector_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def sign(x):
    return -1 if x < 0 else 1 if x > 0 else 0

def segments_intersect(p1, p2, p3, p4):
    d1 = cross_product(vector_sub(p3, p1), vector_sub(p2, p1))
    d2 = cross_product(vector_sub(p4, p1), vector_sub(p2, p1))
    d3 = cross_product(vector_sub(p1, p3), vector_sub(p4, p3))
    d4 = cross_product(vector_sub(p2, p3), vector_sub(p4, p3))
    
    if d1 == 0 and d2 == 0 and d3 == 0 and d4 == 0:
        def on_segment(a, b, c):
            return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and 
                    min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))
        
        return (on_segment(p1, p2, p3) or on_segment(p1, p2, p4) or
                on_segment(p3, p4, p1) or on_segment(p3, p4, p2))
    
    return (sign(d1) != sign(d2) and sign(d3) != sign(d4))

def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
        p1 = tuple(map(int, lines[0].split()))
        p2 = tuple(map(int, lines[1].split()))
        p3 = tuple(map(int, lines[2].split()))
        p4 = tuple(map(int, lines[3].split()))
    
    result = "Yes" if segments_intersect(p1, p2, p3, p4) else "No"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
