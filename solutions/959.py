
import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def point_in_triangle(p, a, b, c):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    d1 = sign(p, a, b)
    d2 = sign(p, b, c)
    d3 = sign(p, c, a)
    
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    
    return not (has_neg and has_pos)

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a, b, c = map(int, data[1].split())
    trees = []
    for i in range(2, 2+n):
        x, y = map(int, data[i].split())
        trees.append((x, y))
    
    max_count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                p1, p2, p3 = trees[i], trees[j], trees[k]
                d1 = dist(p1, p2)
                d2 = dist(p1, p3)
                d3 = dist(p2, p3)
                
                if can_form_triangle(d1, d2, d3):
                    sides = sorted([d1, d2, d3])
                    if math.isclose(sides[0], a) and math.isclose(sides[1], b) and math.isclose(sides[2], c):
                        count = 3
                        for idx, tree in enumerate(trees):
                            if idx != i and idx != j and idx != k:
                                if point_in_triangle(tree, p1, p2, p3):
                                    count += 1
                        if count > max_count:
                            max_count = count
                else:
                    continue
    
    print(max_count)

if __name__ == "__main__":
    main()
