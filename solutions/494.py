
import math

def main():
    x1, y1, x2, y2 = map(int, input().split())
    
    def cross_circle(r):
        a = (x2 - x1)**2 + (y2 - y1)**2
        b = 2 * (x1 * (x2 - x1) + y1 * (y2 - y1))
        c = x1**2 + y1**2 - r**2
        disc = b**2 - 4 * a * c
        
        if disc < 0:
            return 0
            
        t1 = (-b - math.sqrt(disc)) / (2 * a)
        t2 = (-b + math.sqrt(disc)) / (2 * a)
        
        count = 0
        if 0 <= t1 <= 1:
            count += 1
        if 0 <= t2 <= 1 and abs(t1 - t2) > 1e-9:
            count += 1
            
        return count
    
    max_r = max(math.ceil(math.sqrt(x1*x1 + y1*y1)), math.ceil(math.sqrt(x2*x2 + y2*y2)))
    max_r = max(max_r, math.ceil(math.sqrt(max(x1*x1, x2*x2) + max(y1*y1, y2*y2))))
    
    total = 0
    for r in range(1, max_r + 100):
        total += cross_circle(r)
        
    print(total)

if __name__ == "__main__":
    main()
