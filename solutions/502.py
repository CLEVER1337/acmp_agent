
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        a.append(row)
    
    from scipy.optimize import linear_sum_assignment
    import numpy as np
    
    matrix = np.array(a)
    row_ind, col_ind = linear_sum_assignment(matrix, maximize=True)
    total = matrix[row_ind, col_ind].sum()
    print(total)

if __name__ == "__main__":
    main()
