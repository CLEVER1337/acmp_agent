
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    M = []
    for i in range(1, 1+n):
        row = data[i].split()
        M.append([int(x) for x in row])
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if M[i][j] == 1:
                if M[j][i] == 1:
                    count += 1
    
    visited = [False] * n
    order = []
    
    def dfs1(v):
        visited[v] = True
        for u in range(n):
            if M[v][u] == 1 and not visited[u]:
                dfs1(u)
        order.append(v)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
            
    visited2 = [False] * n
    comp = [-1] * n
    comp_count = 0
    
    def dfs2(v, comp_id):
        visited2[v] = True
        comp[v] = comp_id
        for u in range(n):
            if M[u][v] == 1 and not visited2[u]:
                dfs2(u, comp_id)
                
    for i in range(len(order)-1, -1, -1):
        v = order[i]
        if not visited2[v]:
            dfs2(v, comp_count)
            comp_count += 1
            
    scc_edges = set()
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1 and comp[i] != comp[j]:
                scc_edges.add((comp[i], comp[j]))
                
    result = count - len(scc_edges)
    print(result)

if __name__ == "__main__":
    main()
