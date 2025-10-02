
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        matrix.append(row)
    
    max_sum = -10**18
    
    for i in range(n):
        for j in range(n):
            current = matrix[i][j]
            
            if i > 0:
                up = matrix[i-1][j]
                if i > 1:
                    max_sum = max(max_sum, current + up + matrix[i-2][j])
                if j > 0:
                    max_sum = max(max_sum, current + up + matrix[i-1][j-1])
                if j < n-1:
                    max_sum = max(max_sum, current + up + matrix[i-1][j+1])
            
            if i < n-1:
                down = matrix[i+1][j]
                if i < n-2:
                    max_sum = max(max_sum, current + down + matrix[i+2][j])
                if j > 0:
                    max_sum = max(max_sum, current + down + matrix[i+1][j-1])
                if j < n-1:
                    max_sum = max(max_sum, current + down + matrix[i+1][j+1])
            
            if j > 0:
                left = matrix[i][j-1]
                if j > 1:
                    max_sum = max(max_sum, current + left + matrix[i][j-2])
                if i > 0:
                    max_sum = max(max_sum, current + left + matrix[i-1][j-1])
                if i < n-1:
                    max_sum = max(max_sum, current + left + matrix[i+1][j-1])
            
            if j < n-1:
                right = matrix[i][j+1]
                if j < n-2:
                    max_sum = max(max_sum, current + right + matrix[i][j+2])
                if i > 0:
                    max_sum = max(max_sum, current + right + matrix[i-1][j+1])
                if i < n-1:
                    max_sum = max(max_sum, current + right + matrix[i+1][j+1])
    
    print(max_sum)

if __name__ == "__main__":
    main()
