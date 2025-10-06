
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    d = int(data[1])
    graph = [[] for _ in range(n+1)]
    
    index = 2
    for i in range(n-1):
        u = int(data[index]); v = int(data[index+1]); index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        dist = [-1] * (n+1)
        q = deque()
        q.append(start)
        dist[start] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
    
    dist1 = bfs(1)
    max_node = dist1.index(max(dist1))
    dist2 = bfs(max_node)
    diameter = max(dist2)
    
    if diameter < d:
        print(0)
        return
        
    center = max_node
    for i in range(1, n+1):
        if dist2[i] == diameter:
            center = i
            break
            
    dist_center = bfs(center)
    cnt = [0] * (diameter + 2)
    for i in range(1, n+1):
        if dist_center[i] <= diameter:
            cnt[dist_center[i]] += 1
            
    if d % 2 == 0:
        c = d // 2
        center_count = cnt[c]
        if center_count < 3:
            print(0)
            return
            
        total = center_count * (center_count - 1) * (center_count - 2) // 6
        print(total)
    else:
        c1 = d // 2
        c2 = d // 2 + 1
        count1 = cnt[c1]
        count2 = cnt[c2]
        if count1 == 0 or count2 == 0:
            print(0)
            return
            
        total = count1 * count2 * (count1 + count2 - 2) // 2
        print(total)

if __name__ == "__main__":
    main()
