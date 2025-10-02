
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        d, r = map(float, f.readline().split())
        n = int(f.readline().strip())
    
    total_area = math.pi * r * r + 2 * r * d
    
    def area_to_x(area):
        left = 0.0
        right = d + 2 * r
        for _ in range(100):
            mid = (left + right) / 2.0
            area_mid = 0.0
            
            if mid <= r:
                theta = 2 * math.acos((r - mid) / r)
                area_mid = r * r * (theta - math.sin(theta)) / 2
            elif mid >= d + r:
                theta = 2 * math.acos((mid - d - r) / r)
                area_mid = total_area - r * r * (theta - math.sin(theta)) / 2
            else:
                area_left = math.pi * r * r / 2
                if mid > r:
                    theta = 2 * math.acos((mid - r) / r)
                    area_left = r * r * (theta - math.sin(theta)) / 2
                
                area_right = math.pi * r * r / 2
                if d + r - mid > 0:
                    theta = 2 * math.acos((d + r - mid) / r)
                    area_right = r * r * (theta - math.sin(theta)) / 2
                
                area_mid = area_left + (mid - r) * 2 * r + area_right
        
            if area_mid < area:
                left = mid
            else:
                right = mid
        
        return left
    
    results = []
    for i in range(1, n):
        target_area = total_area * i / n
        x = area_to_x(target_area)
        results.append("{:.6f}".format(x))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    main()
