
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
    
    towers_sorted = sorted(towers, key=lambda t: t[0])
    
    result = [0] * n
    
    for i in range(n):
        x_i, h_i, idx_i = towers_sorted[i]
        count = 0
        
        max_tan_left = -float('inf')
        for j in range(i - 1, -1, -1):
            x_j, h_j, idx_j = towers_sorted[j]
            dx = x_i - x_j
            dy = h_j - h_i
            tan_current = dy / dx
            
            if tan_current > max_tan_left:
                count += 1
                max_tan_left = tan_current
        
        max_tan_right = -float('inf')
        for j in range(i + 1, n):
            x_j, h_j, idx_j = towers_sorted[j]
            dx = x_j - x_i
            dy = h_j - h_i
            tan_current = dy / dx
            
            if tan_current > max_tan_right:
                count += 1
                max_tan_right = tan_current
        
        result[idx_i] = count
    
    for count in result:
        print(count)

if __name__ == "__main__":
    main()
