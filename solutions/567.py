
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        r, l, d = map(int, f.readline().split())
    
    R = r * l / (l - r)
    sector_angle = 2 * math.pi * r / math.sqrt(R * R - r * r)
    if sector_angle <= math.pi * 2:
        length = R
    else:
        length = 2 * R
    
    print("{:.6f}".format(length))

if __name__ == "__main__":
    main()
