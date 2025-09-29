
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().splitlines()
    
    n, m = map(int, data[0].split())
    volumes = list(map(int, data[1].split()))
    
    # Инициализация: каждая колба принадлежит своей собственной компоненте
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        
        if rx == ry:
            return
            
        # Газ из колбы с меньшим номером уничтожается
        if rx < ry:
            parent[ry] = rx
            volumes[rx] += volumes[ry]
            volumes[ry] = 0
        else:
            parent[rx] = ry
            volumes[ry] += volumes[rx]
            volumes[rx] = 0
    
    # Обрабатываем все соединения
    for i in range(2, 2 + m):
        a, b = map(int, data[i].split())
        union(a-1, b-1)
    
    # Собираем результаты
    result = []
    for i in range(n):
        if parent[i] == i and volumes[i] > 0:
            result.append((i+1, volumes[i]))
    
    result.sort()
    
    with open("OUTPUT.TXT", "w") as f:
        for num, vol in result:
            f.write(f"{num} {vol}\n")

if __name__ == "__main__":
    main()
