
import sys
from itertools import product

def main():
    data = sys.stdin.read().splitlines()
    index = 0
    parts = data[index].split()
    N = int(parts[0])
    M = int(parts[1])
    index += 1
    
    names = []
    for i in range(N):
        names.append(data[index].strip())
        index += 1
        
    problems = []
    for i in range(M):
        problems.append(data[index].strip())
        index += 1
        
    K = int(data[index])
    index += 1
    
    masks = []
    for i in range(K):
        masks.append(data[index].strip())
        index += 1
        
    P_line = data[index].split()
    P = int(P_line[0])
    symp_indices = set()
    if P > 0:
        symp_indices = set(map(int, P_line[1:1+P]))
    else:
        symp_indices = set()
    
    name_set = set(names)
    problem_set = set(problems)
    
    possible_assignments = []
    for mask in masks:
        parts_mask = mask.split('-')
        if len(parts_mask) < 3:
            possible_assignments.append([])
            continue
            
        a_mask, b_mask, c_mask = parts_mask[0], parts_mask[1], '-'.join(parts_mask[2:])
        
        possible_names = []
        for name in names:
            if len(name) != len(a_mask):
                continue
            match = True
            for i in range(len(name)):
                if a_mask[i] != '?' and a_mask[i] != name[i]:
                    match = False
                    break
            if match:
                possible_names.append(name)
                
        possible_problems = []
        for problem in problems:
            if len(problem) != len(b_mask):
                continue
            match = True
            for i in range(len(problem)):
                if b_mask[i] != '?' and b_mask[i] != problem[i]:
                    match = False
                    break
            if match:
                possible_problems.append(problem)
                
        possible_scores = []
        if all(ch == '?' for ch in c_mask):
            possible_scores = list(range(0, 100000))
        else:
            q_indices = [i for i, ch in enumerate(c_mask) if ch == '?']
            fixed_digits = list(c_mask)
            for digits in product("0123456789", repeat=len(q_indices)):
                for pos, digit in zip(q_indices, digits):
                    fixed_digits[pos] = digit
                num_str = ''.join(fixed_digits)
                if num_str and not num_str.startswith('-'):
                    num = int(num_str)
                    if num >= 0:
                        possible_scores.append(num)
        
        assignments = []
        for name in possible_names:
            for problem in possible_problems:
                for score in possible_scores:
                    assignments.append((name, problem, score))
        possible_assignments.append(assignments)
    
    from collections import defaultdict
    graph = defaultdict(list)
    for i, assignments in enumerate(possible_assignments):
        for name, problem, score in assignments:
            graph[(name, problem)].append((i, score))
    
    best_score = -10**18
    for assignment_comb in product(*possible_assignments):
        used = set()
        valid = True
        total_score = 0
        name_problem_map = {}
        for idx, (name, problem, score) in enumerate(assignment_comb):
            if (name, problem) in used:
                valid = False
                break
            used.add((name, problem))
            name_problem_map[(name, problem)] = score
        
        if not valid:
            continue
            
        participant_scores = defaultdict(int)
        for (name, problem), score in name_problem_map.items():
            participant_scores[name] += score
            
        symp_total = 0
        for i in symp_indices:
            if i-1 < len(names):
                name = names[i-1]
                symp_total += participant_scores[name]
                
        if symp_total > best_score:
            best_score = symp_total
            
    print(best_score)

if __name__ == "__main__":
    main()
