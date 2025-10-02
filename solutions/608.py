
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def segment_intersection(a, b, c, d):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    
    def on_segment(a, b, c):
        if min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1]):
            return True
        return False
    
    o1 = cross(a, c, b)
    o2 = cross(a, c, d)
    o3 = cross(c, a, d)
    o4 = cross(c, b, d)
    
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
        
    if o1 == 0 and on_segment(a, b, c):
        return True
    if o2 == 0 and on_segment(a, b, d):
        return True
    if o3 == 0 and on_segment(c, d, a):
        return True
    if o4 == 0 and on_segment(c, d, b):
        return True
        
    return False

def point_in_obstacle(p, obs):
    x, y = p
    x1, y1, x2, y2 = obs
    return x1 <= x <= x2 and y1 <= y <= y2

def point_on_border(p, obs):
    x, y = p
    x1, y1, x2, y2 = obs
    if (x == x1 or x == x2) and y1 <= y <= y2:
        return True
    if (y == y1 or y == y2) and x1 <= x <= x2:
        return True
    return False

def is_valid_point(p, obstacles):
    for obs in obstacles:
        if point_in_obstacle(p, obs):
            return False
    return True

def can_see(a, b, obstacles):
    for obs in obstacles:
        x1, y1, x2, y2 = obs
        edges = [
            ((x1, y1), (x2, y1)),
            ((x2, y1), (x2, y2)),
            ((x2, y2), (x1, y2)),
            ((x1, y2), (x1, y1))
        ]
        for edge in edges:
            if segment_intersection(a, b, edge[0], edge[1]):
                return False
    return True

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        print("NO")
        return
        
    masha = tuple(map(int, data[0].split()))
    lena = tuple(map(int, data[1].split()))
    n = int(data[2])
    obstacles = []
    for i in range(3, 3 + n):
        parts = list(map(int, data[i].split()))
        obstacles.append(parts)
    
    if can_see(masha, lena, obstacles):
        mid_x = (masha[0] + lena[0]) / 2.0
        mid_y = (masha[1] + lena[1]) / 2.0
        print("YES")
        print(f"{mid_x:.10f} {mid_y:.10f}")
        return
        
    for obs in obstacles:
        x1, y1, x2, y2 = obs
        corners = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        for corner in corners:
            if is_valid_point(corner, obstacles) and can_see(masha, corner, obstacles) and can_see(lena, corner, obstacles):
                print("YES")
                print(f"{corner[0]:.10f} {corner[1]:.10f}")
                return
                
    print("NO")

if __name__ == "__main__":
    solve()
