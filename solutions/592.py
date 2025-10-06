
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    m = int(data[0])
    index = 1
    columns = []
    max_r = 0
    for i in range(m):
        ai = int(data[index]); index += 1
        segments = []
        for j in range(ai):
            l = int(data[index]); r = int(data[index+1]); index += 2
            segments.append((l, r))
            if r > max_r:
                max_r = r
        columns.append(segments)
    
    n = max_r + 2
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
    
    stable = [False] * n
    stable[0] = True
    
    result = []
    for col in columns:
        top = 0
        for seg in col:
            l, r = seg
            if top < r:
                top = r
        if top == 0:
            result.append('0')
            continue
            
        current_top = top
        for seg in reversed(col):
            l, r = seg
            if current_top > r:
                continue
            current_top = l - 1
            break
        
        found = False
        for h in range(top, current_top, -1):
            if stable[find(h)]:
                result.append(str(h))
                found = True
                break
        if not found:
            result.append('0')
            continue
            
        for seg in col:
            l, r = seg
            for h in range(l, r+1):
                union(h, h-1)
                if stable[find(h-1)]:
                    stable[find(h)] = True
                    
    print("\n".join(result))

if __name__ == "__main__":
    main()
