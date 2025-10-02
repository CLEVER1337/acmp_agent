
from itertools import permutations

def get_transpositions(word):
    trans = set()
    n = len(word)
    for i in range(n):
        for j in range(i + 1, n):
            lst = list(word)
            lst[i], lst[j] = lst[j], lst[i]
            trans.add(''.join(lst))
    return trans

def solve():
    letters = input().strip()
    all_words = set(''.join(p) for p in permutations(letters))
    
    selected = set()
    transpositions_cache = {}
    
    for word in sorted(all_words):
        if word in selected:
            continue
            
        word_trans = get_transpositions(word)
        transpositions_cache[word] = word_trans
        
        conflict = False
        for selected_word in selected:
            if word in transpositions_cache[selected_word] or selected_word in word_trans:
                conflict = True
                break
        
        if not conflict:
            selected.add(word)
    
    for word in sorted(selected):
        print(word)

if __name__ == '__main__':
    solve()
