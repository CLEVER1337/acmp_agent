
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points.append((x, y))
    
    result = 0
    
    for i in range(n):
        dist_count = defaultdict(int)
        same_point_count = 0
        
        for j in range(n):
            if i == j:
                continue
                
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist_sq = dx * dx + dy * dy
            
            dist_count[dist_sq] += 1
        
        for count in dist_count.values():
            if count >= 2:
                result += count * (count - 1) // 2
    
    print(result)

if __name__ == "__main__":
    main()
