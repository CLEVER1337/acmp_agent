
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        r, l, d = map(int, f.readline().split())
    
    R = r * l / (l - r)
    h = math.sqrt(l * l - r * r)
    H = math.sqrt(R * R - r * r)
    
    if H <= d:
        length = 2 * R
    else:
        angle = 2 * math.asin(r / R)
        if angle <= math.pi:
            length = 2 * R * math.sin(angle / 2)
        else:
            length = 2 * R
    
    print("{:.6f}".format(length))

if __name__ == '__main__':
    main()
