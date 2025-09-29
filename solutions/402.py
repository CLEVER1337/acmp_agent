
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    if len(points) <= 1:
        return points
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index]); y = int(data[index+1]); index += 2
        points.append((x, y))
    
    if n <= 2:
        print(0)
        return
        
    ch = convex_hull(points)
    m = len(ch)
    
    total = (1 << n) - 2
    invalid = 0
    
    for i in range(m):
        a = ch[i]
        b = ch[(i+1) % m]
        count_on_line = 0
        for p in points:
            if cross(a, b, p) == 0:
                count_on_line += 1
        
        invalid += (1 << count_on_line) - 1
    
    invalid -= (m * (m - 3)) // 2
    
    result = total - invalid
    print(result)

if __name__ == "__main__":
    main()
