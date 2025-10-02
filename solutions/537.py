
import sys
import math
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    M = int(data[1])
    K = int(data[2])
    numbers = list(map(int, data[3:3+n]))
    
    if n == 0:
        print(-1)
        return
        
    numbers.sort()
    
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if math.gcd(numbers[i], numbers[j]) >= K:
                graph[i].append(j)
                graph[j].append(i)
                
    visited = [False] * n
    result = []
    count = [0]
    found = [False]
    target_index = [M]
    
    def backtrack(path):
        if found[0]:
            return
            
        if len(path) == n:
            count[0] += 1
            if count[0] == target_index[0]:
                result.extend([numbers[i] for i in path])
                found[0] = True
            return
            
        last = path[-1] if path else -1
        
        candidates = []
        for neighbor in graph[last] if last != -1 else range(n):
            if not visited[neighbor]:
                if last == -1 or math.gcd(numbers[last], numbers[neighbor]) >= K:
                    candidates.append(neighbor)
                    
        candidates.sort(key=lambda x: numbers[x])
        
        for candidate in candidates:
            if not visited[candidate]:
                visited[candidate] = True
                backtrack(path + [candidate])
                visited[candidate] = False
                if found[0]:
                    return
                    
    backtrack([])
    
    if result:
        print(" ".join(map(str, result)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
