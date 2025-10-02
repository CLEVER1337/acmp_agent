
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    words = data[1:1+2*n]
    
    from collections import defaultdict
    from itertools import permutations, combinations
    
    def is_valid_square(square):
        for i in range(n):
            col_word = ''.join(square[j][i] for j in range(n))
            if col_word not in word_set:
                return False
        return True
    
    word_set = set(words)
    
    for group1 in combinations(words, n):
        group2 = [w for w in words if w not in group1]
        
        for perm1 in permutations(group1):
            if is_valid_square(perm1):
                for perm2 in permutations(group2):
                    if is_valid_square(perm2):
                        square1 = '\n'.join(''.join(row) for row in perm1)
                        square2 = '\n'.join(''.join(row) for row in perm2)
                        print(square1)
                        print()
                        print(square2)
                        return
    
    print("No solution found")

if __name__ == "__main__":
    main()
