
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        top = f.readline().split()
        bottom = f.readline().split()
    
    # Create initial state
    state = top + bottom
    
    # Check if already solved
    solved_state = ['RR', 'BB', 'GG', 'RR', 'BB', 'GG']
    if state == solved_state:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Solved')
        return
    
    # Define moves for 2x2x2 cube
    moves = {
        'F': [3, 0, 1, 2, 4, 5],
        "F'": [1, 2, 3, 0, 4, 5],
        'L': [0, 3, 5, 1, 4, 2],
        "L'": [0, 3, 5, 1, 4, 2],
        'B': [0, 1, 2, 3, 5, 4],
        "B'": [0, 1, 2, 3, 5, 4],
        'R': [0, 1, 2, 3, 4, 5],
        "R'": [0, 1, 2, 3, 4, 5],
        'U': [4, 1, 0, 3, 5, 2],
        "U'": [2, 1, 5, 3, 0, 4],
        'D': [0, 4, 2, 1, 3, 5],
        "D'": [0, 3, 2, 4, 1, 5]
    }
    
    # BFS to find optimal solution
    queue = deque([(state, [])])
    visited = {tuple(state): True}
    
    while queue:
        current_state, path = queue.popleft()
        
        if list(current_state) == solved_state:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(' '.join(path))
            return
        
        for move, permutation in moves.items():
            new_state = [current_state[i] for i in permutation]
            
            if tuple(new_state) not in visited:
                visited[tuple(new_state)] = True
                queue.append((new_state, path + [move]))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('No solution found')

if __name__ == '__main__':
    main()
