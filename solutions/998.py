
import math

def main():
    data = list(map(float, input().split()))
    d, r, x1, y1, x2, y2, u, v = data
    
    def angle(x, y):
        return math.atan2(y, x)
    
    def dist(a, b):
        return math.sqrt(a*a + b*b)
    
    def arc_length(angle_diff):
        return r * min(angle_diff, 2 * math.pi - angle_diff)
    
    a1 = angle(x1, y1)
    a2 = angle(x2, y2 - d)
    
    diff = abs(a1 - a2)
    arc = arc_length(diff)
    time_arc = arc / u
    
    straight_dist = dist(x1 - x2, y1 - y2)
    time_straight = straight_dist / v
    
    option1 = time_arc + time_straight
    
    arc_complement = 2 * math.pi * r / u - time_arc * u
    time_arc_comp = arc_complement / u
    option2 = time_arc_comp + time_straight
    
    print(min(option1, option2))

if __name__ == "__main__":
    main()
