
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    from collections import deque
    import sys
    sys.setrecursionlimit(10000)
    
    n = len(s)
    colors = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    def simulate(state, shot_color, shot_pos):
        if shot_pos == 0:
            new_state = shot_color + state
        else:
            new_state = state[:shot_pos] + shot_color + state[shot_pos:]
        changed = True
        while changed and new_state:
            changed = False
            i = 0
            while i < len(new_state):
                j = i
                while j < len(new_state) and new_state[j] == new_state[i]:
                    j += 1
                if j - i >= 3:
                    new_state = new_state[:i] + new_state[j:]
                    changed = True
                    break
                i = j
        return new_state
    
    memo = {}
    
    def dfs(state):
        if not state:
            return 0, []
        if state in memo:
            return memo[state]
        best_shots = float('inf')
        best_path = []
        for pos in range(len(state)+1):
            for color in colors:
                new_state = simulate(state, color, pos)
                shots, path = dfs(new_state)
                if shots + 1 < best_shots:
                    best_shots = shots + 1
                    best_path = [(color, pos)] + path
        memo[state] = (best_shots, best_path)
        return best_shots, best_path
    
    total_shots, path = dfs(s)
    output = str(total_shots)
    for color, pos in path:
        output += ' ' + color + str(pos)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(output)

if __name__ == '__main__':
    main()
