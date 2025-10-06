
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        top = f.readline().split()
        bottom = f.readline().split()
    
    initial_state = tuple(top + bottom)
    
    if all(color == initial_state[0] for color in initial_state[:4]) and \
       all(color == initial_state[4] for color in initial_state[4:6]) and \
       all(color == initial_state[6] for color in initial_state[6:8]) and \
       all(color == initial_state[8] for color in initial_state[8:10]) and \
       all(color == initial_state[10] for color in initial_state[10:]):
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Solved')
        return
    
    moves = [
        ("F", [2, 0, 3, 1, 4, 5, 6, 7, 8, 9, 11, 10]),
        ("F'", [1, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11]),
        ("L", [0, 4, 2, 3, 5, 1, 6, 7, 8, 9, 10, 11]),
        ("L'", [0, 5, 2, 3, 1, 4, 6, 7, 8, 9, 10, 11]),
        ("B", [0, 1, 6, 2, 4, 5, 7, 3, 8, 9, 10, 11]),
        ("B'", [0, 1, 3, 7, 4, 5, 2, 6, 8, 9, 10, 11]),
        ("R", [0, 1, 2, 8, 4, 5, 6, 7, 9, 3, 10, 11]),
        ("R'", [0, 1, 2, 9, 4, 5, 6, 7, 3, 8, 10, 11]),
        ("U", [0, 1, 2, 3, 10, 4, 6, 7, 8, 9, 5, 11]),
        ("U'", [0, 1, 2, 3, 5, 10, 6, 7, 8, 9, 4, 11]),
        ("D", [0, 1, 2, 3, 4, 5, 11, 6, 8, 9, 10, 7]),
        ("D'", [0, 1, 2, 3, 4, 5, 7, 11, 8, 9, 10, 6])
    ]
    
    def apply_move(state, move_idx):
        new_state = list(state)
        permutation = moves[move_idx][1]
        for i in range(12):
            new_state[i] = state[permutation[i]]
        return tuple(new_state)
    
    def is_solved(state):
        return (state[0] == state[1] == state[2] == state[3] and
                state[4] == state[5] and
                state[6] == state[7] and
                state[8] == state[9] and
                state[10] == state[11])
    
    visited = {}
    queue = deque()
    queue.append((initial_state, []))
    visited[initial_state] = True
    
    while queue:
        state, path = queue.popleft()
        
        if is_solved(state):
            with open('OUTPUT.TXT', 'w') as f:
                if path:
                    f.write(' '.join(path))
                else:
                    f.write('Solved')
            return
        
        for i, (move_name, _) in enumerate(moves):
            new_state = apply_move(state, i)
            if new_state not in visited:
                visited[new_state] = True
                queue.append((new_state, path + [move_name]))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('No solution')

if __name__ == '__main__':
    main()
