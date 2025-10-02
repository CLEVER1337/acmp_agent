
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        x1, y1, x2, y2 = map(int, f.read().split())
    
    def distance_to_origin(x, y):
        return math.sqrt(x*x + y*y)
    
    d1 = distance_to_origin(x1, y1)
    d2 = distance_to_origin(x2, y2)
    
    min_d = min(d1, d2)
    max_d = max(d1, d2)
    
    count = 0
    
    k = math.floor(max_d)
    while k >= math.ceil(min_d):
        if k == 0:
            k -= 1
            continue
            
        r = k
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2
        
        distance = abs(C) / math.sqrt(A*A + B*B)
        
        if distance <= r:
            d1_to_line = abs(A*x1 + B*y1 + C) / math.sqrt(A*A + B*B)
            d2_to_line = abs(A*x2 + B*y2 + C) / math.sqrt(A*A + B*B)
            
            if d1_to_line <= r and d2_to_line <= r:
                count += 1
            else:
                dot1 = x1*x1 + y1*y1
                dot2 = x2*x2 + y2*y2
                if (dot1 <= r*r and dot2 >= r*r) or (dot1 >= r*r and dot2 <= r*r):
                    count += 1
        k -= 1
    
    print(count)

if __name__ == "__main__":
    main()
