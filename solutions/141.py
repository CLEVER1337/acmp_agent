
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
    
    # Проверяем симметричность матрицы (по условию она симметрична)
    # Проверяем отсутствие петель (нули на главной диагонали)
    for i in range(n):
        if matrix[i][i] != 0:
            print("NO")
            return
    
    # Строим список ребер
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                edges.append((i, j))
    
    # Проверяем количество ребер: должно быть n-1 для дерева
    if len(edges) != n - 1:
        print("NO")
        return
    
    # Проверяем связность с помощью BFS/DFS
    visited = [False] * n
    stack = [0]
    visited[0] = True
    count = 1
    
    while stack:
        current = stack.pop()
        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                count += 1
    
    if count == n:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
