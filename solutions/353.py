
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    segments = list(map(int, data[1:1+n]))
    segments.sort(reverse=True)
    
    max_area = 0.0
    for i in range(n - 2):
        a = segments[i]
        b = segments[i + 1]
        c = segments[i + 2]
        
        if a < b + c:
            p = (a + b + c) / 2.0
            area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            if area > max_area:
                max_area = area
    
    print("{:.3f}".format(max_area))

if __name__ == "__main__":
    main()
