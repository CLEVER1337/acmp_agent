
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
    
    possible_entries = []
    for mask in masks:
        parts = mask.split('-')
        if len(parts) < 3:
            possible_entries.append([])
            continue
            
        name_mask, prob_mask, score_mask = parts[0], parts[1], '-'.join(parts[2:])
        
        possible_names = []
        for name in names:
            if len(name) != len(name_mask):
                continue
            match = True
            for i in range(len(name)):
                if name_mask[i] != '?' and name_mask[i] != name[i]:
                    match = False
                    break
            if match:
                possible_names.append(name)
                
        possible_probs = []
        for prob in problems:
            if len(prob) != len(prob_mask):
                continue
            match = True
            for i in range(len(prob)):
                if prob_mask[i] != '?' and prob_mask[i] != prob[i]:
                    match = False
                    break
            if match:
                possible_probs.append(prob)
                
        possible_scores = []
        if all(c == '?' for c in score_mask):
            possible_scores = list(range(0, 100000))
        else:
            score_digits = []
            for char in score_mask:
                if char == '?':
                    score_digits.append([str(i) for i in range(10)])
                else:
                    score_digits.append([char])
            
            for comb in product(*score_digits):
                num_str = ''.join(comb)
                if num_str and not num_str.startswith('0') or len(num_str) == 1:
                    possible_scores.append(int(num_str))
        
        entries = []
        for name in possible_names:
            for prob in possible_probs:
                for score in possible_scores:
                    entries.append((name, prob, score))
        possible_entries.append(entries)
    
    best = -10**18
    
    def backtrack(idx, current_status, used_pairs):
        nonlocal best
        if idx == len(masks):
            total_score = 0
            scores = {name: 0 for name in names}
            for entry in current_status:
                name, prob, score = entry
                scores[name] += score
            for i in symp_set:
                total_score += scores[names[i-1]]
            if total_score > best:
                best = total_score
            return
        
        for entry in possible_entries[idx]:
            name, prob, score = entry
            if (name, prob) not in used_pairs:
                used_pairs.add((name, prob))
                current_status.append(entry)
                backtrack(idx+1, current_status, used_pairs)
                current_status.pop()
                used_pairs.remove((name, prob))
    
    backtrack(0, [], set())
    print(best)

if __name__ == "__main__":
    main()
