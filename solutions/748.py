
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    parents = list(map(int, data[1:1+n-1]))
    
    children = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        parent = parents[i-2]
        children[parent].append(i)
    
    depth = [0] * (n+1)
    q = deque([1])
    while q:
        node = q.popleft()
        for child in children[node]:
            depth[child] = depth[node] + 1
            q.append(child)
    
    max_depth = max(depth)
    colors = [0] * (n+1)
    
    for node in range(1, n+1):
        colors[node] = (depth[node] % max_depth) + 1
    
    print(max_depth)
    print(' '.join(str(colors[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()
