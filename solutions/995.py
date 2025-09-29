
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    R = int(data[0])
    K = int(data[1])
    N = int(data[2])
    
    hairs = []
    index = 3
    for i in range(N):
        xh = float(data[index])
        yh = float(data[index+1])
        xs = float(data[index+2])
        ys = float(data[index+3])
        index += 4
        hairs.append((xh, yh, xs, ys))
    
    def get_angle(xh, yh, xs, ys):
        dx_head = xh
        dy_head = yh
        dx_shoulder = xs
        dy_shoulder = ys + K
        
        angle_head = (dx_head, dy_head)
        angle_shoulder = (dx_shoulder, dy_shoulder)
        
        return (angle_head, angle_shoulder)
    
    hair_angles = []
    for xh, yh, xs, ys in hairs:
        angle_head, angle_shoulder = get_angle(xh, yh, xs, ys)
        hair_angles.append((angle_head, angle_shoulder))
    
    def cross_product(a, b):
        return a[0] * b[1] - a[1] * b[0]
    
    def dot_product(a, b):
        return a[0] * b[0] + a[1] * b[1]
    
    def angle_between(v1, v2):
        cp = cross_product(v1, v2)
        dp = dot_product(v1, v2)
        return cp, dp
    
    count = 0
    for i in range(N):
        head_i, shoulder_i = hair_angles[i]
        for j in range(i + 1, N):
            head_j, shoulder_j = hair_angles[j]
            
            cp1, dp1 = angle_between(head_i, head_j)
            cp2, dp2 = angle_between(shoulder_i, shoulder_j)
            
            if cp1 * cp2 < 0:
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()
