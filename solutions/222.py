
import math

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    obs_x = float(data[1])
    obs_y = float(data[2])
    
    trees = []
    index = 3
    for i in range(n):
        x = float(data[index])
        y = float(data[index+1])
        r = float(data[index+2])
        index += 3
        trees.append((x, y, r))
    
    for x, y, r in trees:
        dx = obs_x - x
        dy = obs_y - y
        dist_sq = dx*dx + dy*dy
        r_sq = r*r
        
        if dist_sq <= r_sq:
            print("NO")
            return
            
    for i in range(n):
        x1, y1, r1 = trees[i]
        for j in range(i + 1, n):
            x2, y2, r2 = trees[j]
            dx = x2 - x1
            dy = y2 - y1
            dist_sq = dx*dx + dy*dy
            sum_r = r1 + r2
            diff_r = abs(r1 - r2)
            
            if dist_sq <= sum_r * sum_r and dist_sq >= diff_r * diff_r:
                print("NO")
                return
                
    print("YES")

if __name__ == "__main__":
    main()
