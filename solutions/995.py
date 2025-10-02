
import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def readfloats():
    return list(map(float, sys.stdin.readline().split()))

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    R, K = readints()
    N = int(data[1])
    
    if N == 0:
        print(0)
        return
        
    hairs = []
    for i in range(2, 2 + N):
        xh, yh, xs, ys = readfloats()
        hairs.append((xh, yh, xs, ys))
    
    def get_angle(xh, yh, xs, ys):
        dx = xs - xh
        dy = ys - yh
        
        angle_head = math.atan2(yh, xh)
        
        if abs(dx) < 1e-12:
            if dy > 0:
                angle_dir = math.pi / 2
            else:
                angle_dir = -math.pi / 2
        else:
            angle_dir = math.atan2(dy, dx)
            
        return angle_head, angle_dir
    
    angle_pairs = []
    for xh, yh, xs, ys in hairs:
        angle_head, angle_dir = get_angle(xh, yh, xs, ys)
        angle_pairs.append((angle_head, angle_dir))
    
    angle_pairs.sort()
    
    count = 0
    n = len(angle_pairs)
    
    for i in range(n):
        head_i, dir_i = angle_pairs[i]
        for j in range(i + 1, n):
            head_j, dir_j = angle_pairs[j]
            
            if dir_i > dir_j:
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()
