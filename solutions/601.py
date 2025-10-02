
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    index = 2
    
    graph = defaultdict(dict)
    
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        c = int(data[index+2])
        index += 3
        
        if c not in graph[u]:
            graph[u][c] = []
        if c not in graph[v]:
            graph[v][c] = []
            
        graph[u][c].append(v)
        graph[v][c].append(u)
    
    k = int(data[index])
    index += 1
    
    colors = []
    if k > 0:
        colors = list(map(int, data[index:index+k]))
    
    current_room = 1
    
    for i, color in enumerate(colors):
        if color not in graph[current_room]:
            print("INCORRECT")
            return
        
        next_rooms = graph[current_room][color]
        if len(next_rooms) > 1:
            print("INCORRECT")
            return
        
        current_room = next_rooms[0]
    
    print(current_room)

if __name__ == "__main__":
    main()
