
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    words = data[1:1+2*n]
    
    from collections import defaultdict
    from itertools import permutations
    
    def is_valid_square(grid):
        for i in range(n):
            col_word = ''.join(grid[j][i] for j in range(n))
            if col_word not in word_set:
                return False
        return True
    
    word_set = set(words)
    
    for perm1 in permutations(words, n):
        remaining = list(set(words) - set(perm1))
        grid1 = list(perm1)
        
        if is_valid_square(grid1):
            for perm2 in permutations(remaining, n):
                grid2 = list(perm2)
                if is_valid_square(grid2):
                    output = []
                    for row in grid1:
                        output.append(row)
                    output.append('')
                    for row in grid2:
                        output.append(row)
                    print('\n'.join(output))
                    return
    
    print("No solution found")

if __name__ == "__main__":
    main()
