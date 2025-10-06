
def main():
    import sys
    from collections import deque
    
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    matrix = []
    index = 1 + n
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        matrix.append(row)
        index += n
    
    initial_state = tuple(A)
    visited = set()
    queue = deque([initial_state])
    visited.add(initial_state)
    
    while queue:
        state = queue.popleft()
        for i in range(n):
            if state[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                if state[j] == 0:
                    continue
                if matrix[i][j] == 0:
                    continue
                
                new_state_list = list(state)
                if matrix[j][i] != 0:
                    option1 = list(state)
                    option1[i] -= 1
                    option1_tuple = tuple(option1)
                    if option1_tuple not in visited:
                        visited.add(option1_tuple)
                        queue.append(option1_tuple)
                    
                    option2 = list(state)
                    option2[j] -= 1
                    option2_tuple = tuple(option2)
                    if option2_tuple not in visited:
                        visited.add(option2_tuple)
                        queue.append(option2_tuple)
                else:
                    new_state_list[j] -= 1
                    new_state_tuple = tuple(new_state_list)
                    if new_state_tuple not in visited:
                        visited.add(new_state_tuple)
                        queue.append(new_state_tuple)
    
    results = sorted(visited)
    print(len(results))
    for res in results:
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
