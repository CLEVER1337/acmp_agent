
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def find_separating_line(seg1, seg2):
    p1, p2 = seg1
    q1, q2 = seg2
    
    for p in [p1, p2]:
        for q in [q1, q2]:
            dx = q[0] - p[0]
            dy = q[1] - p[1]
            
            A = dy
            B = -dx
            C = dx*p[1] - dy*p[0]
            
            if A == 0 and B == 0:
                continue
                
            sign1 = cross((A, B, C), p1, q1)
            sign2 = cross((A, B, C), p1, q2)
            sign3 = cross((A, B, C), p2, q1)
            sign4 = cross((A, B, C), p2, q2)
            
            if sign1 * sign2 <= 0 or sign3 * sign4 <= 0:
                continue
                
            sign_p1 = A*p1[0] + B*p1[1] + C
            sign_p2 = A*p2[0] + B*p2[1] + C
            sign_q1 = A*q1[0] + B*q1[1] + C
            sign_q2 = A*q2[0] + B*q2[1] + C
            
            if sign_p1 * sign_q1 > 0 and sign_p2 * sign_q2 > 0:
                g = gcd(gcd(abs(A), abs(B)), abs(C))
                if g != 0:
                    A //= g
                    B //= g
                    C //= g
                return A, B, C
                
    return None

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    tests = []
    while True:
        line1 = sys.stdin.readline().strip()
        if not line1:
            continue
        data1 = list(map(int, line1.split()))
        if data1 == [0, 0, 0, 0]:
            break
            
        line2 = sys.stdin.readline().strip()
        data2 = list(map(int, line2.split()))
        
        seg1 = [(data1[0], data1[1]), (data1[2], data1[3])]
        seg2 = [(data2[0], data2[1]), (data2[2], data2[3])]
        tests.append((seg1, seg2))
        
    for seg1, seg2 in tests:
        A, B, C = find_separating_line(seg1, seg2)
        print(f"{A} {B} {C}")

if __name__ == "__main__":
    main()
