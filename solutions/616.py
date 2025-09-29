
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    matrix = []
    for i in range(1, 1+n):
        matrix.append(list(map(int, list(data[i].strip()))))
    
    # Проверяем, что отношение рефлексивно? Нет, условие не требует этого
    
    # Построим граф: если R[i][j] = 1, то должно быть f[i] <= g[j]
    # Если R[i][j] = 0, то должно быть f[i] > g[j]
    
    # Создадим списки для f и g
    f = [0] * n
    g = [0] * n
    
    # Построим граф ограничений
    # Для каждой пары (i,j):
    # Если R[i][j] = 1, то f[i] <= g[j]
    # Если R[i][j] = 0, то f[i] > g[j] => g[j] < f[i] => g[j] <= f[i] - 1
    
    # Создадим списки ребер для неравенств
    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges.append((i, j, 0))  # f[i] <= g[j]
            else:
                edges.append((j, i, -1)) # g[j] <= f[i] - 1
    
    # Инициализируем расстояния (используем алгоритм Беллмана-Форда)
    dist = [0] * (2*n)  # первые n - f, следующие n - g
    
    # Добавим фиктивную вершину для инициализации
    for i in range(2*n):
        edges.append((2*n, i, 0))
    
    dist.append(0)
    for _ in range(2*n):
        updated = False
        for u, v, w in edges:
            if u <= 2*n and v <= 2*n:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break
    else:
        # Обнаружен отрицательный цикл
        print("NO")
        return
    
    # Проверим на отрицательные циклы еще раз
    for u, v, w in edges:
        if u <= 2*n and v <= 2*n:
            if dist[u] + w < dist[v]:
                print("NO")
                return
    
    # Извлечем значения f и g
    f_vals = dist[:n]
    g_vals = dist[n:2*n]
    
    # Проверим корректность
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                if f_vals[i] > g_vals[j]:
                    print("NO")
                    return
            else:
                if f_vals[i] <= g_vals[j]:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(map(str, f_vals)))
    print(" ".join(map(str, g_vals)))

if __name__ == "__main__":
    main()
