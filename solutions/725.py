
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    phi0 = float(data[1])
    buildings = []
    idx = 2
    
    for i in range(n):
        x1 = float(data[idx]); y1 = float(data[idx+1])
        x2 = float(data[idx+2]); y2 = float(data[idx+3])
        h = float(data[idx+4])
        idx += 5
        buildings.append((x1, y1, x2, y2, h))
    
    tan_phi0 = math.tan(math.radians(phi0))
    
    def get_corners(x1, y1, x2, y2, h):
        return [
            (x1, y1, h), (x1, y2, h),
            (x2, y1, h), (x2, y2, h)
        ]
    
    def distance(x1, y1, z1, x2, y2, z2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    
    def required_height(gx, gy, gz, px, py, pz):
        dx = px - gx
        dy = py - gy
        dz = pz - gz
        
        if dz <= 0:
            return float('inf')
        
        horizontal_dist = math.sqrt(dx*dx + dy*dy)
        return horizontal_dist / tan_phi0 - dz
    
    def check_height(H):
        gx, gy = 0, 0
        gz = H
        
        for building in buildings:
            x1, y1, x2, y2, h = building
            corners = get_corners(x1, y1, x2, y2, h)
            
            for cx, cy, cz in corners:
                req_h = required_height(gx, gy, gz, cx, cy, cz)
                if req_h > 0:
                    return False
        return True
    
    low = 0.0
    high = 1000000.0
    
    for _ in range(100):
        mid = (low + high) / 2
        if check_height(mid):
            high = mid
        else:
            low = mid
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.6f}".format(high))

if __name__ == "__main__":
    main()
