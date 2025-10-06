
from itertools import permutations

def main():
    s = input().strip()
    perms = set(permutations(s))
    words = [''.join(p) for p in perms]
    
    graph = {}
    for word in words:
        graph[word] = set()
        n = len(word)
        for i in range(n):
            for j in range(i+1, n):
                swapped = list(word)
                swapped[i], swapped[j] = swapped[j], swapped[i]
                neighbor = ''.join(swapped)
                if neighbor != word and neighbor in graph:
                    graph[word].add(neighbor)
                    graph[neighbor].add(word)
    
    independent_sets = []
    current_set = set()
    used = set()
    
    def backtrack(idx):
        if idx == len(words):
            independent_sets.append(current_set.copy())
            return
        
        word = words[idx]
        if word not in used:
            can_add = True
            for neighbor in graph[word]:
                if neighbor in current_set:
                    can_add = False
                    break
            
            if can_add:
                current_set.add(word)
                used.add(word)
                backtrack(idx + 1)
                current_set.remove(word)
                used.remove(word)
            
            backtrack(idx + 1)
        else:
            backtrack(idx + 1)
    
    backtrack(0)
    
    max_set = max(independent_sets, key=len)
    for word in sorted(max_set):
        print(word)

if __name__ == "__main__":
    main()
