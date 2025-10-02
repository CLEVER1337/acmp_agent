
import math

def main():
    data = list(map(float, input().split()))
    d, r, x1, y1, x2, y2, u, v = data
    
    def angle(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        return math.atan2(dy, dx)
    
    def point_on_circle(center, radius, angle):
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        return (x, y)
    
    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    
    center1 = (0.0, 0.0)
    center2 = (0.0, d)
    
    home = (x1, y1)
    school = (x2, y2)
    
    angle1 = angle(center1, home)
    angle2 = angle(center2, school)
    
    direct_angle = angle(center1, center2)
    
    def time_on_circle(angle_start, angle_end, radius, speed):
        diff = abs(angle_end - angle_start)
        diff = min(diff, 2 * math.pi - diff)
        arc_length = diff * radius
        return arc_length / speed
    
    def total_time(exit_angle1, entry_angle2):
        exit_point1 = point_on_circle(center1, r, exit_angle1)
        entry_point2 = point_on_circle(center2, r, entry_angle2)
        
        time1 = time_on_circle(angle1, exit_angle1, r, u)
        time2 = distance(exit_point1, entry_point2) / v
        time3 = time_on_circle(entry_angle2, angle2, r, u)
        
        return time1 + time2 + time3
    
    def f(alpha):
        theta = math.atan2(d - r * math.sin(alpha), r * math.cos(alpha))
        return total_time(alpha, theta)
    
    left = direct_angle - math.pi / 2
    right = direct_angle + math.pi / 2
    
    for _ in range(100):
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if f(m1) < f(m2):
            right = m2
        else:
            left = m1
    
    result = f((left + right) / 2)
    
    print("{:.10f}".format(result))

if __name__ == "__main__":
    main()
