
def point_in_rectangle(px, py, rect):
    x1, y1, x2, y2, x3, y3, x4, y4 = rect
    
    def cross_product(ax, ay, bx, by, cx, cy):
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    
    def sign(x):
        return 1 if x >= 0 else -1
    
    cross1 = cross_product(x1, y1, x2, y2, px, py)
    cross2 = cross_product(x2, y2, x3, y3, px, py)
    cross3 = cross_product(x3, y3, x4, y4, px, py)
    cross4 = cross_product(x4, y4, x1, y1, px, py)
    
    sign1 = sign(cross1)
    sign2 = sign(cross2)
    sign3 = sign(cross3)
    sign4 = sign(cross4)
    
    return sign1 == sign2 == sign3 == sign4

def main():
    import sys
    data = sys.stdin.read().split()
    
    n = int(data[0])
    index = 1
    count = 0
    
    for _ in range(n):
        coords = list(map(int, data[index:index+10]))
        index += 10
        
        x, y = coords[0], coords[1]
        rect = coords[2:]
        
        if point_in_rectangle(x, y, rect):
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()
