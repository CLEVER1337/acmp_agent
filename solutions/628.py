
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    villages = []
    index = 1
    
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        villages.append((x, y))
    
    x1 = villages[0][0]
    x2 = villages[1][0]
    
    left = min(x1, x2)
    right = max(x1, x2)
    
    def total_distance(x):
        total = 0.0
        for village in villages:
            dx = village[0] - x
            dy = village[1] - 0
            total += (dx**2 + dy**2)**0.5
        return total
    
    low = left
    high = right
    
    for _ in range(100):
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        
        d1 = total_distance(mid1)
        d2 = total_distance(mid2)
        
        if d1 < d2:
            high = mid2
        else:
            low = mid1
    
    optimal_x = (low + high) / 2
    print("{:.6f}".format(optimal_x))

if __name__ == "__main__":
    main()
