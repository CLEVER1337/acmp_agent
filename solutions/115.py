
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        matrix.append(row)
    
    max_sum = -float('inf')
    
    for top in range(n):
        temp = [0] * m
        for bottom in range(top, n):
            for j in range(m):
                temp[j] += matrix[bottom][j]
                
            current_sum = 0
            best_in_row = -float('inf')
            for num in temp:
                current_sum = max(num, current_sum + num)
                best_in_row = max(best_in_row, current_sum)
                
            max_sum = max(max_sum, best_in_row)
    
    print(max_sum)

if __name__ == "__main__":
    main()
