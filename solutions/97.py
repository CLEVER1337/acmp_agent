
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    rectangles = []
    index = 1
    for i in range(n):
        x1 = int(data[index]); y1 = int(data[index+1]); x2 = int(data[index+2]); y2 = int(data[index+3]); R = int(data[index+4])
        index += 5
        
        left = min(x1, x2) - R
        right = max(x1, x2) + R
        bottom = min(y1, y2) - R
        top = max(y1, y2) + R
        
        rectangles.append((left, bottom, right, top))
    
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            parent[ry] = rx
    
    for i in range(n):
        for j in range(i + 1, n):
            a_left, a_bottom, a_right, a_top = rectangles[i]
            b_left, b_bottom, b_right, b_top = rectangles[j]
            
            if not (a_right < b_left or b_right < a_left or a_top < b_bottom or b_top < a_bottom):
                union(i, j)
    
    roots = set()
    for i in range(n):
        roots.add(find(i))
    
    print(len(roots))

if __name__ == "__main__":
    main()
