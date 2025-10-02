
from collections import deque

def main():
    with open('INPUT.TXT', 'r') as f:
        top = f.readline().split()
        bottom = f.readline().split()
    
    state = top + bottom
    
    if all(state[i][0] == state[i][1] for i in range(6)):
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Solved')
        return
    
    moves = ['F', 'F\'', 'L', 'L\'', 'B', 'B\'', 'R', 'R\'', 'U', 'U\'', 'D', 'D\'']
    
    def apply_move(s, move):
        new_state = s[:]
        if move == 'F':
            new_state[0] = s[0][1] + s[0][0]
            new_state[1] = s[4][0] + s[1][1]
            new_state[4] = s[3][1] + s[4][1]
            new_state[3] = s[5][0] + s[3][0]
            new_state[5] = s[1][0] + s[5][1]
        elif move == 'F\'':
            new_state[0] = s[0][1] + s[0][0]
            new_state[1] = s[5][0] + s[1][1]
            new_state[4] = s[1][0] + s[4][1]
            new_state[3] = s[4][1] + s[3][0]
            new_state[5] = s[3][1] + s[5][1]
        elif move == 'L':
            new_state[1] = s[1][1] + s[1][0]
            new_state[0] = s[5][1] + s[0][1]
            new_state[2] = s[0][0] + s[2][1]
            new_state[5] = s[2][0] + s[5][0]
            new_state[4] = s[4][0] + s[4][1]
        elif move == 'L\'':
            new_state[1] = s[1][1] + s[1][0]
            new_state[0] = s[2][0] + s[0][1]
            new_state[2] = s[5][1] + s[2][1]
            new_state[5] = s[0][0] + s[5][0]
            new_state[4] = s[4][0] + s[4][1]
        elif move == 'B':
            new_state[2] = s[2][1] + s[2][0]
            new_state[1] = s[1][0] + s[4][1]
            new_state[4] = s[4][0] + s[3][0]
            new_state[3] = s[3][1] + s[5][1]
            new_state[5] = s[5][0] + s[1][1]
        elif move == 'B\'':
            new_state[2] = s[2][1] + s[2][0]
            new_state[1] = s[1][0] + s[5][1]
            new_state[4] = s[4][0] + s[1][1]
            new_state[3] = s[3][1] + s[4][1]
            new_state[5] = s[5][0] + s[3][0]
        elif move == 'R':
            new_state[3] = s[3][1] + s[3][0]
            new_state[0] = s[0][0] + s[4][0]
            new_state[2] = s[2][0] + s[5][0]
            new_state[4] = s[4][1] + s[2][1]
            new_state[5] = s[5][1] + s[0][1]
        elif move == 'R\'':
            new_state[3] = s[3][1] + s[3][0]
            new_state[0] = s[0][0] + s[5][1]
            new_state[2] = s[2][0] + s[4][1]
            new_state[4] = s[4][1] + s[0][1]
            new_state[5] = s[5][1] + s[2][1]
        elif move == 'U':
            new_state[4] = s[4][1] + s[4][0]
            new_state[0] = s[3][0] + s[0][1]
            new_state[1] = s[0][0] + s[1][1]
            new_state[2] = s[1][0] + s[2][1]
            new_state[3] = s[2][0] + s[3][1]
        elif move == 'U\'':
            new_state[4] = s[4][1] + s[4][0]
            new_state[0] = s[1][0] + s[0][1]
            new_state[1] = s[2][0] + s[1][1]
            new_state[2] = s[3][0] + s[2][1]
            new_state[3] = s[0][0] + s[3][1]
        elif move == 'D':
            new_state[5] = s[5][1] + s[5][0]
            new_state[0] = s[0][0] + s[1][1]
            new_state[1] = s[1][0] + s[2][1]
            new_state[2] = s[2][0] + s[3][1]
            new_state[3] = s[3][0] + s[0][1]
        elif move == 'D\'':
            new_state[5] = s[5][1] + s[5][0]
            new_state[0] = s[0][0] + s[3][1]
            new_state[1] = s[1][0] + s[0][1]
            new_state[2] = s[2][0] + s[1][1]
            new_state[3] = s[3][0] + s[2][1]
        return new_state
    
    def is_solved(s):
        return all(s[i][0] == s[i][1] for i in range(6))
    
    visited = {}
    queue = deque()
    queue.append((state, []))
    visited[''.join(state)] = True
    
    while queue:
        current_state, path = queue.popleft()
        
        if is_solved(current_state):
            with open('OUTPUT.TXT', 'w') as f:
                f.write(' '.join(path))
            return
        
        for move in moves:
            new_state = apply_move(current_state, move)
            state_str = ''.join(new_state)
            if state_str not in visited:
                visited[state_str] = True
                queue.append((new_state, path + [move]))

if __name__ == '__main__':
    main()
