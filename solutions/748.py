
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
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for child in children[node]:
            depth[child] = depth[node] + 1
            queue.append(child)
    
    max_depth = max(depth)
    colors = [0] * (n+1)
    
    for node in range(1, n+1):
        colors[node] = depth[node] % 2 + 1
    
    k = 2 if max_depth >= 1 else 1
    
    print(k)
    print(' '.join(map(str, colors[1:])))

if __name__ == "__main__":
    main()
