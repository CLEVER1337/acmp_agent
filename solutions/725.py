
import math

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    phi0_deg = float(data[1])
    phi0 = math.radians(phi0_deg)
    tan_phi0 = math.tan(phi0)
    
    buildings = []
    index = 2
    for i in range(n):
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        h = int(data[index+4])
        index += 5
        buildings.append((x1, y1, x2, y2, h))
    
    left = 0.0
    right = 1000000.0
    
    for _ in range(100):
        mid = (left + right) / 2.0
        valid = True
        
        for building in buildings:
            x1, y1, x2, y2, h_building = building
            corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            protected = False
            
            for cx, cy in corners:
                dx = abs(cx)
                dy = abs(cy)
                dist = math.sqrt(dx*dx + dy*dy)
                required_height = dist * tan_phi0 - mid
                if required_height < h_building:
                    protected = True
                    break
            
            if not protected:
                valid = False
                break
        
        if valid:
            right = mid
        else:
            left = mid
    
    print("{:.6f}".format(left))

if __name__ == "__main__":
    main()
