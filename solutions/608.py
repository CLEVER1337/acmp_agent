
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    x1, y1 = float(data[0]), float(data[1])
    x2, y2 = float(data[2]), float(data[3])
    n = int(data[4])
    
    obstacles = []
    index = 5
    for i in range(n):
        x_min = float(data[index])
        y_min = float(data[index+1])
        x_max = float(data[index+2])
        y_max = float(data[index+3])
        obstacles.append((x_min, y_min, x_max, y_max))
        index += 4
        
    def point_in_obstacle(x, y):
        for (x_min, y_min, x_max, y_max) in obstacles:
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return True
        return False
        
    def segments_intersect(a, b, c, d):
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
            
        def on_segment(a, b, c):
            return min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
            
        o1 = cross(a, b, c)
        o2 = cross(a, b, d)
        o3 = cross(c, d, a)
        o4 = cross(c, d, b)
        
        if o1 == 0 and on_segment(a, b, c):
            return True
        if o2 == 0 and on_segment(a, b, d):
            return True
        if o3 == 0 and on_segment(c, d, a):
            return True
        if o4 == 0 and on_segment(c, d, b):
            return True
            
        return o1 * o2 < 0 and o3 * o4 < 0
        
    def line_intersects_obstacle(p1, p2):
        for (x_min, y_min, x_max, y_max) in obstacles:
            corners = [(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)]
            for i in range(4):
                a = corners[i]
                b = corners[(i+1)%4]
                if segments_intersect(p1, p2, a, b):
                    return True
        return False
        
    def can_see(p1, p2):
        if not line_intersects_obstacle(p1, p2):
            return True
        return False
        
    def find_good_point():
        if can_see((x1, y1), (x2, y2)):
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            if not point_in_obstacle(mid_x, mid_y):
                return mid_x, mid_y
                
        points_to_check = []
        points_to_check.append((x1, y1))
        points_to_check.append((x2, y2))
        
        for obs in obstacles:
            x_min, y_min, x_max, y_max = obs
            corners = [(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)]
            for corner in corners:
                points_to_check.append(corner)
                
        for i in range(len(points_to_check)):
            for j in range(i+1, len(points_to_check)):
                p1 = points_to_check[i]
                p2 = points_to_check[j]
                if can_see(p1, (x1, y1)) and can_see(p1, (x2, y2)) and not point_in_obstacle(p1[0], p1[1]):
                    return p1[0], p1[1]
                if can_see(p2, (x1, y1)) and can_see(p2, (x2, y2)) and not point_in_obstacle(p2[0], p2[1]):
                    return p2[0], p2[1]
                    
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                for point in points_to_check:
                    test_x = point[0] + dx * 1e-5
                    test_y = point[1] + dy * 1e-5
                    if not point_in_obstacle(test_x, test_y):
                        if can_see((test_x, test_y), (x1, y1)) and can_see((test_x, test_y), (x2, y2)):
                            return test_x, test_y
        return None
        
    result_point = find_good_point()
    if result_point:
        print("YES")
        print("{:.10f} {:.10f}".format(result_point[0], result_point[1]))
    else:
        print("NO")

if __name__ == "__main__":
    main()
