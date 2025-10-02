
def point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    d1 = sign((x, y), (x1, y1), (x2, y2))
    d2 = sign((x, y), (x2, y2), (x3, y3))
    d3 = sign((x, y), (x3, y3), (x1, y1))
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)

def main():
    import sys
    data = sys.stdin.read().split()
    
    xn = float(data[0])
    yn = float(data[1])
    k = int(data[2])
    
    countries = []
    index = 3
    for i in range(k):
        coords = list(map(float, data[index:index+6]))
        countries.append(coords)
        index += 6
    
    result = []
    for i, country in enumerate(countries, 1):
        x1, y1, x2, y2, x3, y3 = country
        if point_in_triangle(xn, yn, x1, y1, x2, y2, x3, y3):
            result.append(i)
    
    print(len(result))
    if result:
        print(" ".join(map(str, result)))
    else:
        print()

if __name__ == "__main__":
    main()
