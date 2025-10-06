
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    words = data[1:1+2*n]
    
    def is_valid_square(grid):
        for i in range(n):
            vertical_word = ''.join(grid[j][i] for j in range(n))
            if vertical_word not in word_set:
                return False
        return True
    
    def backtrack(grid, used, row):
        if row == n:
            return grid[:]
            
        for word in words:
            if used[word] >= count[word]:
                continue
                
            valid = True
            for col in range(n):
                if grid[col][row] != word[col]:
                    valid = False
                    break
                    
            if valid:
                used[word] += 1
                grid[row] = word
                result = backtrack(grid, used, row + 1)
                if result:
                    return result
                used[word] -= 1
                grid[row] = None
                
        return None
    
    from collections import defaultdict
    count = defaultdict(int)
    for word in words:
        count[word] += 1
        
    word_set = set(words)
    
    grid1 = [None] * n
    used = defaultdict(int)
    square1 = backtrack(grid1, used, 0)
    
    remaining_words = []
    for word in words:
        if used[word] < count[word]:
            remaining_words.append(word)
            
    count2 = defaultdict(int)
    for word in remaining_words:
        count2[word] += 1
        
    word_set2 = set(remaining_words)
    grid2 = [None] * n
    used2 = defaultdict(int)
    square2 = backtrack(grid2, used2, 0)
    
    for row in square1:
        print(row)
    print()
    for row in square2:
        print(row)

if __name__ == "__main__":
    main()
