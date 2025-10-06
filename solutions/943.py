
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        M = int(data[1])
        Y = int(data[2])
        X = int(data[3])
    
    matrix = [[0] * M for _ in range(N)]
    
    top = 0
    bottom = N - 1
    left = 0
    right = M - 1
    num = 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(matrix[Y-1][X-1]))

if __name__ == "__main__":
    main()
