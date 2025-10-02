
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
    
    result = [0] * n
    
    for i in range(n):
        count = 0
        x_i, h_i, idx_i = towers[i]
        
        max_slope_left = float('-inf')
        for j in range(i - 1, -1, -1):
            x_j, h_j, idx_j = towers[j]
            dx = x_i - x_j
            dy = h_j - h_i
            slope = dy / dx
            
            if slope > max_slope_left:
                max_slope_left = slope
                count += 1
        
        max_slope_right = float('-inf')
        for j in range(i + 1, n):
            x_j, h_j, idx_j = towers[j]
            dx = x_j - x_i
            dy = h_j - h_i
            slope = dy / dx
            
            if slope > max_slope_right:
                max_slope_right = slope
                count += 1
        
        result[idx_i] = count
    
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
