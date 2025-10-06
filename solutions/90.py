
import sys

def readints():
    return list(map(int, sys.stdin.read().split()))

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_in_triangle(pt, v1, v2, v3):
    d1 = sign(pt, v1, v2)
    d2 = sign(pt, v2, v3)
    d3 = sign(pt, v3, v1)
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)

def main():
    data = readints()
    idx = 0
    x, y = data[idx], data[idx+1]
    idx += 2
    k = data[idx]
    idx += 1
    
    city = (x, y)
    countries = []
    result = []
    
    for i in range(k):
        coords = data[idx:idx+6]
        idx += 6
        v1 = (coords[0], coords[1])
        v2 = (coords[2], coords[3])
        v3 = (coords[4], coords[5])
        countries.append((v1, v2, v3))
    
    for i in range(k):
        v1, v2, v3 = countries[i]
        if point_in_triangle(city, v1, v2, v3):
            result.append(i+1)
    
    print(len(result))
    if result:
        print(" ".join(map(str, result)))
    else:
        print()

if __name__ == "__main__":
    main()
