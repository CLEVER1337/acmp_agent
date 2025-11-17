
from collections import defaultdict
import sys
sys.setrecursionlimit(20000)

def dfs_loop(graph, visited, stack):
    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, vertex, visited, stack)
    return stack

def dfs(graph, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(vertex)

def transpose_graph(graph):
    g = defaultdict(list)
    for vertex in graph:
        for neighbor in graph[vertex]:
            g[neighbor].append(vertex)
    return g

def get_scc(graph, stack):
    visited = {v: False for v in graph}
    scc = []
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs(graph, vertex, visited, component)
            scc.append(component)
    return scc

def solve_problem():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, r = map(int, input().split())
        if r == 1:
            graph[u].append(v)
    visited = {v: False for v in graph}
    stack = dfs_loop(graph, visited, [])
    t_graph = transpose_graph(graph)
    scc = get_scc(t_graph, stack)
    result = []
    for component in scc:
        if len(component) % 2 == 0 and len(component) == n-1:
            result.extend(component)
    if len(result) != n-1:
        print(-1)
    else:
        result.sort()
        for road in result:
            print(road)

if __name__ == "__main__":
    solve_problem()
