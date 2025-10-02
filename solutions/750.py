
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n1 = int(data[0])
    n2 = int(data[1])
    m = int(data[2])
    
    n = n1 + n2
    graph = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    index = 3
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    win = [''] * (n + 1)
    q = deque()
    
    for i in range(1, n + 1):
        if deg[i] == 0:
            win[i] = 'P'
            q.append(i)
    
    while q:
        u = q.popleft()
        for v in graph[u]:
            if win[v] != '':
                continue
            if win[u] == 'P':
                win[v] = 'N'
                q.append(v)
            else:
                deg[v] -= 1
                if deg[v] == 0:
                    win[v] = 'P'
                    q.append(v)
    
    res1 = []
    for i in range(1, n1 + 1):
        if win[i] == 'N':
            res1.append('N')
        else:
            res1.append('P')
            
    res2 = []
    for i in range(n1 + 1, n1 + n2 + 1):
        if win[i] == 'N':
            res2.append('N')
        else:
            res2.append('P')
            
    print(''.join(res1))
    print(''.join(res2))

if __name__ == "__main__":
    main()
