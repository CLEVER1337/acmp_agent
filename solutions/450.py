
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    matrix = []
    for i in range(1, n+1):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    from itertools import permutations
    
    total_bottles_per_type = [0] * n
    for j in range(n):
        for i in range(n):
            total_bottles_per_type[j] += matrix[i][j]
    
    best_perm = None
    min_moves = float('inf')
    
    for perm in permutations(range(n)):
        moves = 0
        for i in range(n):
            target_type = perm[i]
            moves += total_bottles_per_type[target_type] - matrix[i][target_type]
        
        if moves < min_moves:
            min_moves = moves
            best_perm = perm
    
    letters = [chr(ord('A') + i) for i in best_perm]
    output_perm = ' '.join(letters)
    
    print(output_perm)
    print(min_moves)

if __name__ == "__main__":
    main()
