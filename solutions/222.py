
import math

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    obs_x = float(data[1])
    obs_y = float(data[2])
    
    trees = []
    index = 3
    for i in range(n):
        x = float(data[index])
        y = float(data[index+1])
        r = float(data[index+2])
        index += 3
        trees.append((x, y, r))
    
    for tree in trees:
        x, y, r = tree
        dx = obs_x - x
        dy = obs_y - y
        dist = math.sqrt(dx*dx + dy*dy)
        
        if dist <= r:
            print("NO")
            return
    
    angles = []
    for tree in trees:
        x, y, r = tree
        dx = x - obs_x
        dy = y - obs_y
        dist = math.sqrt(dx*dx + dy*dy)
        
        angle_center = math.atan2(dy, dx)
        angle_half = math.asin(r / dist)
        
        start_angle = angle_center - angle_half
        end_angle = angle_center + angle_half
        
        angles.append((start_angle, end_angle))
    
    for i in range(len(angles)):
        start1, end1 = angles[i]
        while end1 < start1:
            end1 += 2 * math.pi
        
        for j in range(i + 1, len(angles)):
            start2, end2 = angles[j]
            while end2 < start2:
                end2 += 2 * math.pi
            
            if start1 <= start2 <= end1 or start1 <= end2 <= end1:
                continue
            if start2 <= start1 <= end2 or start2 <= end1 <= end2:
                continue
            
            if start1 + 2 * math.pi <= end2 or start2 + 2 * math.pi <= end1:
                continue
                
            print("NO")
            return
    
    print("YES")

if __name__ == "__main__":
    main()
