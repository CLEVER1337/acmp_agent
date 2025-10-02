
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    matrix = []
    for i in range(1, n+1):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    total_moves = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                total_moves += matrix[i][j]
    
    letters = [chr(ord('a') + i) for i in range(n)]
    permutation = ''.join(letters).upper()
    
    print(permutation)
    print(total_moves)

if __name__ == "__main__":
    main()
