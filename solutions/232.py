
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    trees = []
    index = 1
    for i in range(n):
        x = float(data[index])
        y = float(data[index+1])
        r = float(data[index+2])
        index += 3
        trees.append((x, y, r))
    
    if n <= 2:
        print("YES")
        return
        
    def circles_intersect(c1, c2):
        x1, y1, r1 = c1
        x2, y2, r2 = c2
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return dist <= r1 + r2
        
    def point_in_circle(px, py, circle):
        x, y, r = circle
        return math.sqrt((px - x)**2 + (py - y)**2) <= r
        
    def line_circle_intersect(line_start, line_end, circle):
        x0, y0, r = circle
        x1, y1 = line_start
        x2, y2 = line_end
        
        dx = x2 - x1
        dy = y2 - y1
        a = dx**2 + dy**2
        b = 2 * (dx * (x1 - x0) + dy * (y1 - y0))
        c = (x1 - x0)**2 + (y1 - y0)**2 - r**2
        
        discriminant = b**2 - 4 * a * c
        
        if discriminant < 0:
            return False
            
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
        return (0 <= t1 <= 1) or (0 <= t2 <= 1)
        
    for i in range(n):
        for j in range(i + 1, n):
            if not circles_intersect(trees[i], trees[j]):
                continue
                
            x1, y1, r1 = trees[i]
            x2, y2, r2 = trees[j]
            
            dx = x2 - x1
            dy = y2 - y1
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist < abs(r1 - r2):
                continue
                
            a = r1
            b = dist
            c = r2
            
            cos_alpha = (a**2 + b**2 - c**2) / (2 * a * b)
            alpha = math.acos(cos_alpha)
            
            dx_norm = dx / dist
            dy_norm = dy / dist
            
            tangent1_x = x1 + r1 * math.cos(alpha) * dx_norm - r1 * math.sin(alpha) * dy_norm
            tangent1_y = y1 + r1 * math.sin(alpha) * dx_norm + r1 * math.cos(alpha) * dy_norm
            
            tangent2_x = x1 + r1 * math.cos(-alpha) * dx_norm - r1 * math.sin(-alpha) * dy_norm
            tangent2_y = y1 + r1 * math.sin(-alpha) * dx_norm + r1 * math.cos(-alpha) * dy_norm
            
            valid_line1 = True
            valid_line2 = True
            
            for k in range(n):
                if k == i or k == j:
                    continue
                    
                if line_circle_intersect((tangent1_x, tangent1_y), (tangent2_x, tangent2_y), trees[k]):
                    valid_line1 = False
                    break
                    
            if valid_line1:
                print("NO")
                return
                
            for k in range(n):
                if k == i or k == j:
                    continue
                    
                if line_circle_intersect((tangent1_x, tangent1_y), (tangent2_x, tangent2_y), trees[k]):
                    valid_line2 = False
                    break
                    
            if valid_line2:
                print("NO")
                return
                
    print("YES")

if __name__ == "__main__":
    main()
