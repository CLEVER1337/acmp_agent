
import sys

def readints():
    return list(map(int, sys.stdin.read().split()))

def vec(a, b):
    return (b[0] - a[0], b[1] - a[1])

def cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def length(v):
    return (v[0]**2 + v[1]**2)**0.5

def normalize(v):
    l = length(v)
    if l == 0:
        return (0, 0)
    return (v[0]/l, v[1]/l)

def angle_between(v1, v2):
    cos_theta = dot(normalize(v1), normalize(v2))
    return cos_theta

def triangle_signature(triangle):
    a, b, c = triangle
    ab = vec(a, b)
    ac = vec(a, c)
    bc = vec(b, c)
    
    sides = sorted([length(ab), length(ac), length(bc)])
    angles = sorted([
        angle_between(ab, ac),
        angle_between(vec(b, a), vec(b, c)),
        angle_between(vec(c, a), vec(c, b))
    ])
    
    return (sides, angles)

def main():
    data = readints()
    n = data[0]
    triangles = []
    index = 1
    
    for i in range(n):
        points = []
        for j in range(3):
            x = data[index]
            y = data[index+1]
            index += 2
            points.append((x, y))
        triangles.append(points)
    
    if n == 0:
        print("YES")
        return
        
    base_signature = triangle_signature(triangles[0])
    
    for i in range(1, n):
        current_signature = triangle_signature(triangles[i])
        
        sides1, angles1 = base_signature
        sides2, angles2 = current_signature
        
        if len(sides1) != len(sides2):
            print("NO")
            return
            
        for j in range(len(sides1)):
            if abs(sides1[j] - sides2[j]) > 1e-9:
                print("NO")
                return
                
        for j in range(len(angles1)):
            if abs(angles1[j] - angles2[j]) > 1e-9:
                print("NO")
                return
                
    print("YES")

if __name__ == "__main__":
    main()
