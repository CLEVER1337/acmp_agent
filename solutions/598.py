
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    graph = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        graph.append(row)
    
    max_group_size = 0
    best_assignment = None
    
    def is_valid(group, person):
        for member in group:
            if graph[person][member] == 0:
                return False
        return True
    
    def backtrack(assignment, groups, person_idx):
        nonlocal max_group_size, best_assignment
        
        if person_idx == n:
            current_max = max(len(group) for group in groups)
            if current_max > max_group_size:
                max_group_size = current_max
                best_assignment = assignment.copy()
            return
        
        for group_id in range(len(groups)):
            if len(groups[group_id]) < 5 and is_valid(groups[group_id], person_idx):
                groups[group_id].append(person_idx)
                assignment[person_idx] = group_id
                backtrack(assignment, groups, person_idx + 1)
                groups[group_id].pop()
        
        if len(groups) < n:
            new_group_id = len(groups)
            groups.append([person_idx])
            assignment[person_idx] = new_group_id
            backtrack(assignment, groups, person_idx + 1)
            groups.pop()
    
    assignment = [0] * n
    groups = [[]]
    backtrack(assignment, groups, 0)
    
    group_count = max(best_assignment) + 1
    print(group_count)
    print(' '.join(str(x + 1) for x in best_assignment))

if __name__ == "__main__":
    main()
