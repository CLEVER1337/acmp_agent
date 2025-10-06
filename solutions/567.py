
import math

def main():
    r, l, d = map(int, input().split())
    
    if l <= d:
        h = math.sqrt(l * l - r * r)
        result = h + r
    else:
        h = math.sqrt(l * l - r * r)
        if r + h <= d:
            result = h + r
        else:
            theta = math.acos(d / l)
            phi = math.asin(r / l)
            alpha = math.pi - theta - phi
            if alpha <= 0:
                result = h + r
            else:
                arc_length = alpha * r
                result = h + arc_length
    
    print("{:.6f}".format(result))

if __name__ == "__main__":
    main()
