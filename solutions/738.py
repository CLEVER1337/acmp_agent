
from itertools import permutations
from collections import defaultdict

def get_transpositions(word):
    transpositions = set()
    n = len(word)
    for i in range(n):
        for j in range(i + 1, n):
            lst = list(word)
            lst[i], lst[j] = lst[j], lst[i]
            transpositions.add(''.join(lst))
    return transpositions

def solve():
    s = input().strip()
    all_words = set([''.join(p) for p in permutations(s)])
    
    graph = defaultdict(set)
    for word in all_words:
        trans = get_transpositions(word)
        for t in trans:
            if t in all_words and t != word:
                graph[word].add(t)
                graph[t].add(word)
    
    independent_set = set()
    remaining = all_words.copy()
    
    while remaining:
        word = min(remaining, key=lambda x: len(graph[x] & remaining))
        independent_set.add(word)
        remaining.remove(word)
        neighbors = graph[word] & remaining
        remaining -= neighbors
    
    for word in independent_set:
        print(word)

solve()
