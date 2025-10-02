
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    H = int(data[0])
    W = int(data[1])
    N = int(data[2])
    
    index = 3
    grid = []
    for i in range(H):
        row = list(map(int, data[index:index+W]))
        index += W
        grid.append(row)
    
    # Создаем матрицу префиксных сумм
    prefix = [[0] * (W + 1) for _ in range(H + 1)]
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    results = []
    for i in range(N):
        ai = int(data[index])
        bi = int(data[index+1])
        ci = int(data[index+2])
        di = int(data[index+3])
        index += 4
        
        # Вычисляем сумму прямоугольной области с использованием префиксных сумм
        total = prefix[ci][di] - prefix[ai-1][di] - prefix[ci][bi-1] + prefix[ai-1][bi-1]
        results.append(str(total))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
