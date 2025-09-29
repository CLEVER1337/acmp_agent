
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    
    graph = defaultdict(dict)
    
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); c = int(data[idx+2]); idx += 3
        if c not in graph[u]:
            graph[u][c] = []
        graph[u][c].append(v)
        
        if c not in graph[v]:
            graph[v][c] = []
        graph[v][c].append(u)
    
    k = int(data[idx]); idx += 1
    
    colors = []
    if k > 0:
        colors = list(map(int, data[idx:idx+k]))
    
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
