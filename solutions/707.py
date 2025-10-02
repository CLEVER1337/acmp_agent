
def main():
    with open('INPUT.TXT', 'r') as f:
        initial = f.readline().strip()
    
    from collections import deque
    import heapq

    def remove_groups(state):
        changed = True
        while changed:
            changed = False
            n = len(state)
            if n < 3:
                break
            i = 0
            while i < n:
                j = i
                while j < n and state[j] == state[i]:
                    j += 1
                if j - i >= 3:
                    state = state[:i] + state[j:]
                    changed = True
                    break
                i = j
        return state

    visited = set()
    heap = []
    heapq.heappush(heap, (len(initial), 0, initial, []))
    best_moves = None
    best_len = float('inf')
    
    while heap:
        cost, shots, state, moves = heapq.heappop(heap)
        if state == "":
            if len(moves) < best_len:
                best_len = len(moves)
                best_moves = moves
            continue
        
        if len(moves) >= 10:
            continue
            
        state_str = state
        if state_str in visited:
            continue
        visited.add(state_str)
        
        n = len(state)
        for pos in range(0, n+1):
            for color in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                new_state = state[:pos] + color + state[pos:]
                new_state = remove_groups(new_state)
                new_moves = moves + [(color, pos)]
                heapq.heappush(heap, (len(new_state), len(new_moves), new_state, new_moves))
    
    if best_moves is None:
        print("0")
    else:
        result = str(len(best_moves))
        for move in best_moves:
            result += f" {move[0]}{move[1]}"
        with open('OUTPUT.TXT', 'w') as f:
            f.write(result)

if __name__ == "__main__":
    main()
