
import math

def main():
    data = input().split()
    d = float(data[0])
    r = float(data[1])
    n = int(input())
    
    total_area = math.pi * r * r + 2 * r * d
    
    def f(x):
        if x <= r:
            return math.pi * r * r / 2 - (r * r * math.acos(x / r) - x * math.sqrt(r * r - x * x))
        elif x <= d + r:
            return (x - r) * 2 * r
        else:
            segment_area = total_area - f(d + r - (x - (d + r)))
            return total_area - segment_area
    
    target_area = total_area / n
    results = []
    
    for i in range(1, n):
        target = target_area * i
        low = 0.0
        high = d + 2 * r
        
        for _ in range(100):
            mid = (low + high) / 2.0
            area = f(mid)
            if area < target:
                low = mid
            else:
                high = mid
        
        results.append("{:.6f}".format((low + high) / 2.0))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
