
import math

def main():
    with open("INPUT.TXT", "r") as f:
        lines = f.readlines()
        xk, yk = map(float, lines[0].split())
        xc, yc, rc = map(float, lines[1].split())
    
    d = math.sqrt((xk - xc)**2 + (yk - yc)**2)
    
    if d >= rc:
        area = math.pi * rc * rc
    else:
        theta = 2 * math.acos(d / rc)
        segment_area = (rc * rc / 2) * (theta - math.sin(theta))
        area = math.pi * rc * rc - segment_area
    
    with open("OUTPUT.TXT", "w") as f:
        f.write("{:.3f}".format(area))

if __name__ == "__main__":
    main()
