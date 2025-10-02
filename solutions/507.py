
def main():
    import sys
    from itertools import product
    
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    matrix = []
    idx = 1 + n
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        matrix.append(row)
        idx += n
    
    possible_states = set()
    stack = [tuple(A)]
    
    while stack:
        current = stack.pop()
        if current in possible_states:
            continue
        possible_states.add(current)
        
        found_interaction = False
        for i in range(n):
            for j in range(n):
                if current[i] > 0 and current[j] > 0:
                    if matrix[i][j] == 1 and matrix[j][i] == 1:
                        if i != j:
                            if current[i] > 0 and current[j] > 0:
                                new_state1 = list(current)
                                new_state1[i] -= 1
                                if new_state1[i] < 0:
                                    new_state1[i] = 0
                                stack.append(tuple(new_state1))
                                
                                new_state2 = list(current)
                                new_state2[j] -= 1
                                if new_state2[j] < 0:
                                    new_state2[j] = 0
                                stack.append(tuple(new_state2))
                                found_interaction = True
                    elif matrix[i][j] == 1:
                        if current[i] > 0 and current[j] > 0:
                            new_state = list(current)
                            new_state[j] -= 1
                            if new_state[j] < 0:
                                new_state[j] = 0
                            stack.append(tuple(new_state))
                            found_interaction = True
    
    possible_states_list = sorted(possible_states)
    print(len(possible_states_list))
    for state in possible_states_list:
        print(' '.join(map(str, state)))

if __name__ == "__main__":
    main()
