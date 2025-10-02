
import sys
from itertools import product

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    names = [data[i+1].strip() for i in range(n)]
    problems = [data[i+n+1].strip() for i in range(m)]
    k = int(data[n+m+1])
    masks = [data[i+n+m+2].strip() for i in range(k)]
    p = int(data[n+m+k+2])
    symp = list(map(int, data[n+m+k+3].split()))
    
    symp_set = set(symp)
    
    possible_scores = {}
    for name in names:
        for problem in problems:
            possible_scores[(name, problem)] = []
    
    for mask in masks:
        parts = mask.split('-')
        if len(parts) < 3:
            continue
            
        name_mask, problem_mask, score_mask = parts[0], parts[1], parts[2]
        
        for name in names:
            if len(name_mask) != len(name):
                continue
            match_name = True
            for i, char in enumerate(name_mask):
                if char != '?' and char != name[i]:
                    match_name = False
                    break
            if not match_name:
                continue
                
            for problem in problems:
                if len(problem_mask) != len(problem):
                    continue
                match_problem = True
                for i, char in enumerate(problem_mask):
                    if char != '?' and char != problem[i]:
                        match_problem = False
                        break
                if not match_problem:
                    continue
                    
                if score_mask == '?':
                    possible_scores[(name, problem)].append((0, float('inf')))
                else:
                    score_min = 0
                    score_max = 0
                    valid_score = True
                    for char in score_mask:
                        if char == '?':
                            score_min = score_min * 10
                            score_max = score_max * 10 + 9
                        elif '0' <= char <= '9':
                            digit = int(char)
                            score_min = score_min * 10 + digit
                            score_max = score_max * 10 + digit
                        else:
                            valid_score = False
                            break
                    if valid_score:
                        possible_scores[(name, problem)].append((score_min, score_max))
    
    max_possible = {}
    for (name, problem), ranges in possible_scores.items():
        if ranges:
            max_val = max(max_val for _, max_val in ranges)
            max_possible[(name, problem)] = max_val
        else:
            max_possible[(name, problem)] = 0
    
    best_score = 0
    for assignment in product(*[possible_scores.get((name, problem), [(0, 0)]) for name in names for problem in problems]):
        scores = {}
        idx = 0
        valid = True
        for i, name in enumerate(names):
            for j, problem in enumerate(problems):
                min_val, max_val = assignment[idx]
                if min_val > max_val:
                    valid = False
                    break
                score_val = max_val
                if (name, problem) in scores:
                    valid = False
                    break
                scores[(name, problem)] = score_val
                idx += 1
            if not valid:
                break
        
        if not valid:
            continue
            
        total = 0
        for i in symp_set:
            name = names[i-1]
            for problem in problems:
                total += scores.get((name, problem), 0)
        
        if total > best_score:
            best_score = total
    
    print(best_score)

if __name__ == "__main__":
    main()
