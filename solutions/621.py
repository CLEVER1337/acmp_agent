
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n = int(data[0].strip())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, data[i].strip().split()))
        matrix.append(row)
    
    result = [row[:] for row in matrix]
    zeros = []
    non_zeros = []
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros.append((i, j))
            else:
                non_zeros.append((i, j))
    
    if not zeros or not non_zeros:
        for row in result:
            print(' '.join(map(str, row)))
        return
    
    for zi, zj in zeros:
        min_dist = float('inf')
        candidates = []
        
        for ni, nj in non_zeros:
            dist = abs(zi - ni) + abs(zj - nj)
            if dist < min_dist:
                min_dist = dist
                candidates = [(ni, nj)]
            elif dist == min_dist:
                candidates.append((ni, nj))
        
        if len(candidates) == 1:
            ni, nj = candidates[0]
            result[zi][zj] = matrix[ni][nj]
    
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
