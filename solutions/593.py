
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    towers = []
    index = 1
    for i in range(n):
        x = int(data[index])
        h = int(data[index + 1])
        index += 2
        towers.append((x, h, i))
    
    towers.sort(key=lambda t: t[0])
    x_coords = [t[0] for t in towers]
    heights = [t[1] for t in towers]
    indices = [t[2] for t in towers]
    
    result = [0] * n
    
    for i in range(n):
        count = 0
        if i > 0:
            max_slope = -10**18
            for j in range(i - 1, -1, -1):
                dx = x_coords[i] - x_coords[j]
                dy = heights[i] - heights[j]
                slope = dy / dx
                if slope > max_slope:
                    max_slope = slope
                    count += 1
        
        if i < n - 1:
            min_slope = 10**18
            for j in range(i + 1, n):
                dx = x_coords[j] - x_coords[i]
                dy = heights[j] - heights[i]
                slope = dy / dx
                if slope < min_slope:
                    min_slope = slope
                    count += 1
        
        result[indices[i]] = count
    
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
