
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        matrix.append(row)
    
    if k == 1:
        print(matrix[0][0])
        return
        
    max_val = max(max(row) for row in matrix)
    
    if k % 2 == 0:
        result = max(matrix[0][0] + max_val, 2 * max_val)
        for step in range(2, k, 2):
            result = max(result, (step // 2 + 1) * max_val + (step // 2) * max_val)
        print(result)
    else:
        neighbors = []
        if n > 1:
            neighbors.append(matrix[1][0])
            neighbors.append(matrix[0][1])
        max_neighbor = max(neighbors) if neighbors else matrix[0][0]
        
        result = max(matrix[0][0] + max_neighbor, max_val + max_neighbor)
        for step in range(3, k, 2):
            half = step // 2
            result = max(result, (half + 1) * max_val + half * max_val)
        print(result)

if __name__ == "__main__":
    main()
