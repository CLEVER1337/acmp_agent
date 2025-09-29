
import sys

def read_input(file_path):
    with open(file_path, 'r') as f:
        content = f.read().split('\n\n')
    tests = []
    for block in content:
        lines = block.strip().split('\n')
        if not lines:
            continue
        if lines[0] == '0 0':
            break
        n, k = map(int, lines[0].split())
        sets = []
        for i in range(1, 1 + k):
            parts = lines[i].split()
            if parts:
                s = list(map(int, parts))
                sets.append(s)
        tests.append((n, k, sets))
    return tests

def find_next_partition(n, sets):
    elements = [0] * (n + 1)
    group_id = [0] * (n + 1)
    groups = []
    
    for idx, s in enumerate(sets):
        group = []
        for num in s:
            elements[num] = 1
            group_id[num] = idx
            group.append(num)
        groups.append(group)
    
    free_elems = [i for i in range(1, n + 1) if elements[i] == 0]
    if free_elems:
        return None
    
    max_group = -1
    elem_to_move = -1
    for i in range(n, 0, -1):
        current_gid = group_id[i]
        if current_gid > max_group:
            max_group = current_gid
        else:
            for j in range(current_gid + 1, max_group + 1):
                for num in groups[j]:
                    if num > i:
                        elem_to_move = i
                        target_gid = j
                        break
                if elem_to_move != -1:
                    break
            if elem_to_move != -1:
                break
    if elem_to_move == -1:
        return None
    
    source_gid = group_id[elem_to_move]
    groups[source_gid].remove(elem_to_move)
    groups[target_gid].append(elem_to_move)
    groups[target_gid].sort()
    
    new_groups = []
    for g in groups[:target_gid + 1]:
        if g:
            new_groups.append(g)
    
    remaining_elems = []
    for g in groups[target_gid + 1:]:
        remaining_elems.extend(g)
    
    if remaining_elems:
        remaining_elems.sort()
        new_groups.append(remaining_elems)
    
    for i in range(source_gid + 1, target_gid):
        if groups[i]:
            new_groups.append(groups[i])
    
    new_groups.sort(key=lambda x: x[0])
    return new_groups

def main():
    input_data = read_input('INPUT.TXT')
    output_lines = []
    
    for n, k, sets in input_data:
        next_partition = find_next_partition(n, sets)
        if next_partition is None:
            next_partition = []
            for i in range(1, n + 1):
                next_partition.append([i])
            next_partition.sort(key=lambda x: x[0])
        
        output_lines.append(f"{n} {len(next_partition)}")
        for s in next_partition:
            output_lines.append(' '.join(map(str, s)))
        output_lines.append('')
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(output_lines))

if __name__ == '__main__':
    main()
