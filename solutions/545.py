
import math

def main():
    data = input().split()
    a, b, c = map(float, data)
    sides = sorted([a, b, c])
    
    def is_right_triangle(x, y, z):
        return abs(x*x + y*y - z*z) < 1e-9
    
    if is_right_triangle(sides[0], sides[1], sides[2]):
        area = 0.5 * sides[0] * sides[1]
        print("{:.15f}".format(area))
        return
    
    max_area = 0.0
    
    def calculate_area(hyp, leg1, leg2):
        if hyp <= 0 or leg1 <= 0 or leg2 <= 0:
            return 0.0
        if leg1 + leg2 <= hyp:
            return 0.0
        
        x = (leg1 * leg1 - leg2 * leg2 + hyp * hyp) / (2 * hyp)
        if x < 0 or x > hyp:
            return 0.0
        
        if x > leg1:
            return 0.0
        
        height = math.sqrt(leg1 * leg1 - x * x)
        area = 0.5 * hyp * height
        return area
    
    max_area = max(max_area, calculate_area(a, b, c))
    max_area = max(max_area, calculate_area(a, c, b))
    max_area = max(max_area, calculate_area(b, a, c))
    max_area = max(max_area, calculate_area(b, c, a))
    max_area = max(max_area, calculate_area(c, a, b))
    max_area = max(max_area, calculate_area(c, b, a))
    
    print("{:.15f}".format(max_area))

if __name__ == "__main__":
    main()
