
from collections import deque

def solve():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        if not data:
            print("IMPOSSIBLE")
            return
            
        B1, B2, B3, T = map(int, data)
    
    def bfs():
        visited = set()
        queue = deque([(B1, 0, 0, 0)])
        visited.add((B1, 0, 0))
        
        while queue:
            state = queue.popleft()
            a, b, c, steps = state
            
            if a == T:
                return steps
            
            next_states = []
            
            if a > 0:
                if b < B2:
                    pour = min(a, B2 - b)
                    next_states.append((a - pour, b + pour, c, steps + 1))
                if c < B3:
                    pour = min(a, B3 - c)
                    next_states.append((a - pour, b, c + pour, steps + 1))
            
            if b > 0:
                if a < B1:
                    pour = min(b, B1 - a)
                    next_states.append((a + pour, b - pour, c, steps + 1))
                if c < B3:
                    pour = min(b, B3 - c)
                    next_states.append((a, b - pour, c + pour, steps + 1))
            
            if c > 0:
                if a < B1:
                    pour = min(c, B1 - a)
                    next_states.append((a + pour, b, c - pour, steps + 1))
                if b < B2:
                    pour = min(c, B2 - b)
                    next_states.append((a, b + pour, c - pour, steps + 1))
            
            for state in next_states:
                key = (state[0], state[1], state[2])
                if key not in visited:
                    visited.add(key)
                    queue.append(state)
        
        return -1
    
    result = bfs()
    with open('OUTPUT.TXT', 'w') as f:
        if result == -1:
            f.write("IMPOSSIBLE")
        else:
            f.write(str(result))

solve()
