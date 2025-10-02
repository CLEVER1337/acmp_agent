
import sys
import math

def point_to_segment_distance(px, py, x1, y1, x2, y2):
    line_length_sq = (x2 - x1)**2 + (y2 - y1)**2
    if line_length_sq == 0:
        return math.sqrt((px - x1)**2 + (py - y1)**2)
    
    t = max(0, min(1, ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / line_length_sq))
    proj_x = x1 + t * (x2 - x1)
    proj_y = y1 + t * (y2 - y1)
    return math.sqrt((px - proj_x)**2 + (py - proj_y)**2)

def solve_segment(x11, y11, x12, y12, x21, y21, x22, y22):
    if (x11, y11, x12, y12) == (0, 0, 0, 0) and (x21, y21, x22, y22) == (0, 0, 0, 0):
        return None
    
    mid1_x = (x11 + x12) / 2.0
    mid1_y = (y11 + y12) / 2.0
    mid2_x = (x21 + x22) / 2.0
    mid2_y = (y21 + y22) / 2.0
    
    center_x = (mid1_x + mid2_x) / 2.0
    center_y = (mid1_y + mid2_y) / 2.0
    
    dist1 = point_to_segment_distance(center_x, center_y, x11, y11, x12, y12)
    dist2 = point_to_segment_distance(center_x, center_y, x21, y21, x22, y22)
    
    radius = max(dist1, dist2) * 1.0001
    
    return center_x, center_y, radius

def main():
    data = sys.stdin.read().split()
    index = 0
    results = []
    
    while index < len(data):
        x11 = int(data[index]); y11 = int(data[index+1]); x12 = int(data[index+2]); y12 = int(data[index+3])
        index += 4
        x21 = int(data[index]); y21 = int(data[index+1]); x22 = int(data[index+2]); y22 = int(data[index+3])
        index += 4
        
        if x11 == 0 and y11 == 0 and x12 == 0 and y12 == 0 and x21 == 0 and y21 == 0 and x22 == 0 and y22 == 0:
            break
            
        result = solve_segment(x11, y11, x12, y12, x21, y21, x22, y22)
        if result:
            results.append(result)
    
    for center_x, center_y, radius in results:
        print(f"{center_x:.6f} {center_y:.6f} {radius:.6f}")

if __name__ == "__main__":
    main()
