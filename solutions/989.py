
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def solve():
    while True:
        line1 = sys.stdin.readline().strip()
        if not line1:
            line1 = sys.stdin.readline().strip()
        if not line1:
            break
            
        data1 = list(map(int, line1.split()))
        if data1 == [0,0,0,0]:
            break
            
        data2 = list(map(int, sys.stdin.readline().split()))
        if data2 == [0,0,0,0]:
            break
            
        trench1 = [(data1[0], data1[1]), (data1[2], data1[3])]
        trench2 = [(data2[0], data2[1]), (data2[2], data2[3])]
        
        p1, p2 = trench1
        q1, q2 = trench2
        
        if cross(p1, p2, q1) * cross(p1, p2, q2) > 0:
            a = p2[1] - p1[1]
            b = p1[0] - p2[0]
            c = p2[0]*p1[1] - p1[0]*p2[1]
            
            if a*q1[0] + b*q1[1] + c > 0:
                a, b, c = -a, -b, -c
                
            print(a, b, c)
        else:
            a = q2[1] - q1[1]
            b = q1[0] - q2[0]
            c = q2[0]*q1[1] - q1[0]*q2[1]
            
            if a*p1[0] + b*p1[1] + c > 0:
                a, b, c = -a, -b, -c
                
            print(a, b, c)

solve()
