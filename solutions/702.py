
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    rects = []
    index = 1
    for i in range(n):
        x1 = int(data[index]); y1 = int(data[index+1])
        x2 = int(data[index+2]); y2 = int(data[index+3])
        index += 4
        rects.append((x1, y1, x2, y2))
    
    def dfs(i, visited, group):
        visited[i] = True
        group.append(i)
        for j in range(n):
            if not visited[j]:
                x1_i, y1_i, x2_i, y2_i = rects[i]
                x1_j, y1_j, x2_j, y2_j = rects[j]
                
                x_overlap = not (x2_i <= x1_j or x2_j <= x1_i)
                y_overlap = not (y2_i <= y1_j or y2_j <= y1_i)
                
                x_touch = (x2_i == x1_j or x2_j == x1_i) and y_overlap
                y_touch = (y2_i == y1_j or y2_j == y1_i) and x_overlap
                
                if (x_overlap and y_overlap) or x_touch or y_touch:
                    dfs(j, visited, group)
    
    max_area = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            group = []
            dfs(i, visited, group)
            
            min_x = min(rects[i][0] for i in group)
            max_x = max(rects[i][2] for i in group)
            min_y = min(rects[i][1] for i in group)
            max_y = max(rects[i][3] for i in group)
            
            area = (max_x - min_x) * (max_y - min_y)
            max_area = max(max_area, area)
    
    print(max_area)

if __name__ == "__main__":
    main()
