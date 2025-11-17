
from heapq import *

def solve(n, m, r, preferences):
    # Создаем граф
    graph = [[] for _ in range(r)]
    for i in range(r):
        a, b, c = preferences[i]
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    # Инициализируем очередь с приоритетами и множество посещенных вершин
    queue = [(0, 0)]
    visited = set()
    
    total_cost = 0
    mst_edges = []
    
    # Пока очередь не пуста...
    while queue:
        cost, node = heappop(queue)
        
        if node not in visited:
            visited.add(node)
            total_cost += cost
            
            for next_cost, next_node in graph[node]:
                if next_node not in visited:
                    heappush(queue, (next_cost, next_node))
                    
    # Возвращаем стоимость и количество ребер в MST
    return total_cost, len(mst_edges), [i+1 for i in range(len(mst_edges))]

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    preferences = []
    for _ in range(r):
        a, b, c = map(int, input().split())
        preferences.append((a-1, b-1, c))  # индексы начинаются с 0
    
    total_cost, num_tickets, tickets = solve(n, m, r, preferences)
    print(total_cost)
    print(num_tickets)
    print(' '.join(map(str, tickets)))
