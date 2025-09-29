
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        x1, y1, x2, y2 = map(int, f.read().split())
    
    def distance_to_line(x0, y0):
        dx = x2 - x1
        dy = y2 - y1
        length_sq = dx*dx + dy*dy
        
        if length_sq == 0:
            return math.sqrt((x0-x1)**2 + (y0-y1)**2)
        
        t = max(0, min(1, ((x0-x1)*dx + (y0-y1)*dy) / length_sq))
        proj_x = x1 + t * dx
        proj_y = y1 + t * dy
        return math.sqrt((x0-proj_x)**2 + (y0-proj_y)**2)
    
    count = 0
    max_r = max(abs(x1), abs(y1), abs(x2), abs(y2)) + 1
    
    for r in range(1, max_r + 1):
        d = distance_to_line(0, 0)
        
        if d > r:
            continue
            
        if d == r:
            count += 1
        else:
            d1 = math.sqrt(x1*x1 + y1*y1)
            d2 = math.sqrt(x2*x2 + y2*y2)
            
            if (d1 <= r and d2 >= r) or (d1 >= r and d2 <= r):
                count += 1
            elif d1 < r and d2 < r:
                pass
            else:
                count += 2
    
    print(count)

if __name__ == '__main__':
    main()
