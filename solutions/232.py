
import math

def read_input():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        trees = []
        for _ in range(n):
            data = list(map(float, f.readline().split()))
            trees.append((data[0], data[1], data[2]))
        return trees

def write_output(result):
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def line_circle_intersection(x1, y1, x2, y2, cx, cy, r):
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    
    dist = abs(A * cx + B * cy + C) / math.sqrt(A**2 + B**2)
    return dist <= r

def check_forest(trees):
    n = len(trees)
    
    if n <= 2:
        return "YES"
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, r1 = trees[i]
            x2, y2, r2 = trees[j]
            
            dx = x2 - x1
            dy = y2 - y1
            d = distance(x1, y1, x2, y2)
            
            if d <= r1 + r2:
                continue
            
            for k in range(n):
                if k == i or k == j:
                    continue
                
                cx, cy, cr = trees[k]
                if line_circle_intersection(x1, y1, x2, y2, cx, cy, cr):
                    break
            else:
                left_count = 0
                right_count = 0
                
                A = y2 - y1
                B = x1 - x2
                C = x2 * y1 - x1 * y2
                
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    cx, cy, cr = trees[k]
                    value = A * cx + B * cy + C
                    
                    if value > 0:
                        left_count += 1
                    elif value < 0:
                        right_count += 1
                
                if left_count > 0 and right_count > 0:
                    return "NO"
    
    return "YES"

trees = read_input()
result = check_forest(trees)
write_output(result)
