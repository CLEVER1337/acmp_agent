
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        grid.append(row)
    
    from scipy.optimize import linear_sum_assignment
    cost_matrix = []
    for j in range(n):
        col = []
        for i in range(n):
            col.append(-grid[i][j])
        cost_matrix.append(col)
    
    cost_matrix = list(map(list, zip(*cost_matrix)))
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    total = 0
    for i, j in zip(row_ind, col_ind):
        total += grid[i][j]
    
    print(total)

if __name__ == "__main__":
    main()
