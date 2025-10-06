
import math

def main():
    data = []
    while True:
        try:
            line = input().split()
            if not line:
                continue
            data.append(line)
        except EOFError:
            break
            
    xk, yk = map(float, data[0])
    xc, yc, rc = map(float, data[1])
    
    dx = xk - xc
    dy = yk - yc
    d = math.sqrt(dx*dx + dy*dy)
    
    if d >= rc:
        area = math.pi * rc * rc
    else:
        h = rc - d
        segment_area = rc * rc * math.acos((rc - h) / rc) - (rc - h) * math.sqrt(2 * rc * h - h * h)
        area = math.pi * rc * rc - segment_area
        
    print("{:.3f}".format(area))

if __name__ == "__main__":
    main()
