
import math

def main():
    data = list(map(float, input().split()))
    d, r, x1, y1, x2, y2, u, v = data
    
    def angle(p, center=(0, 0)):
        return math.atan2(p[1] - center[1], p[0] - center[0])
    
    def point_on_circle(angle, center=(0, 0)):
        return (center[0] + r * math.cos(angle), center[1] + r * math.sin(angle))
    
    home = (x1, y1)
    school = (x2, y2)
    center1 = (0, 0)
    center2 = (0, d)
    
    theta1 = angle(home, center1)
    theta2 = angle(school, center2)
    
    def time_between_angles(theta_a, theta_b, center_from, center_to):
        arc_angle = abs(theta_a - theta_b)
        if arc_angle > math.pi:
            arc_angle = 2 * math.pi - arc_angle
        
        arc_length = r * arc_angle
        arc_time = arc_length / u
        
        point_a = point_on_circle(theta_a, center_from)
        point_b = point_on_circle(theta_b, center_to)
        
        field_dist = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
        field_time = field_dist / v
        
        return arc_time + field_time
    
    time1 = time_between_angles(theta1, theta2, center1, center2)
    time2 = time_between_angles(theta1, theta2 + math.pi, center1, center2)
    time3 = time_between_angles(theta1 + math.pi, theta2, center1, center2)
    time4 = time_between_angles(theta1 + math.pi, theta2 + math.pi, center1, center2)
    
    min_time = min(time1, time2, time3, time4)
    
    print("{:.10f}".format(min_time))

if __name__ == "__main__":
    main()
