
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        points.append((x, y))
    
    if n < 2:
        print(0)
        return
        
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            line = (points[i][0], points[i][1], points[j][0], points[j][1])
            a = points[j][1] - points[i][1]
            b = points[i][0] - points[j][0]
            c = points[i][0] * (points[i][1] - points[j][1]) + points[i][1] * (points[j][0] - points[i][0])
            
            left_pink = 0
            right_pink = 0
            left_blue = 0
            right_blue = 0
            
            valid = True
            for k in range(n):
                if k == i or k == j:
                    continue
                    
                value = a * points[k][0] + b * points[k][1] + c
                if value == 0:
                    valid = False
                    break
                    
                if value > 0:
                    left_pink += 1
                    left_blue += 1
                else:
                    right_pink += 1
                    right_blue += 1
            
            if not valid:
                continue
                
            if left_pink > 0 and right_pink > 0:
                total += 1
            if left_blue > 0 and right_blue > 0:
                total += 1
                
    print(total)

if __name__ == "__main__":
    main()
