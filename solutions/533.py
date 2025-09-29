
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
    
    count = 0
    
    for i in range(n):
        distances = defaultdict(int)
        same_points = 0
        
        for j in range(n):
            if i == j:
                continue
                
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist_sq = dx * dx + dy * dy
            
            if dist_sq == 0:
                same_points += 1
            else:
                distances[dist_sq] += 1
        
        for dist, cnt in distances.items():
            count += cnt * (cnt - 1) // 2
        
        count += same_points * (same_points - 1) // 2
    
    print(count)

if __name__ == "__main__":
    main()
