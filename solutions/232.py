
import math

def read_input():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    trees = []
    index = 1
    for i in range(n):
        x = float(data[index])
        y = float(data[index+1])
        r = float(data[index+2])
        index += 3
        trees.append((x, y, r))
    return trees

def point_to_line_distance(p, line):
    x0, y0 = p
    a, b, c = line
    return abs(a*x0 + b*y0 + c) / math.sqrt(a*a + b*b)

def check_line_clearance(trees, line):
    for tree in trees:
        x, y, r = tree
        dist = point_to_line_distance((x, y), line)
        if dist < r - 1e-9:
            return False
    return True

def check_forest(trees):
    n = len(trees)
    if n <= 1:
        return True
        
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1 = trees[i]
            x2, y2, r2 = trees[j]
            
            dx = x2 - x1
            dy = y2 - y1
            d = math.sqrt(dx*dx + dy*dy)
            
            if d <= abs(r1 - r2) + 1e-9:
                continue
                
            angle = math.atan2(dy, dx)
            alpha = math.asin((r1 + r2) / d)
            
            for sign in [-1, 1]:
                theta = angle + sign * alpha
                a = -math.sin(theta)
                b = math.cos(theta)
                c = -a*x1 - b*y1
                
                if check_line_clearance(trees, (a, b, c)):
                    return False
                    
                c = -a*x2 - b*y2
                if check_line_clearance(trees, (a, b, c)):
                    return False
                    
            if d > abs(r1 - r2):
                beta = math.asin((r1 - r2) / d)
                for sign in [-1, 1]:
                    theta = angle + sign * beta
                    a = -math.sin(theta)
                    b = math.cos(theta)
                    c = -a*x1 - b*y1
                    
                    if check_line_clearance(trees, (a, b, c)):
                        return False
                        
                    c = -a*x2 - b*y2
                    if check_line_clearance(trees, (a, b, c)):
                        return False
    
    for i in range(n):
        x, y, r = trees[i]
        for angle in [0, math.pi/4, math.pi/2, 3*math.pi/4]:
            a = -math.sin(angle)
            b = math.cos(angle)
            c = -a*x - b*y
            if check_line_clearance(trees, (a, b, c)):
                return False
                
    return True

def main():
    trees = read_input()
    if check_forest(trees):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
