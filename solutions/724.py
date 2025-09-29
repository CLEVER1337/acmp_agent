
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("Impossible")
        return
        
    n = int(data[0])
    m = int(data[1])
    idx = 2
    matrix = []
    for i in range(n):
        row = list(map(int, data[idx:idx+m]))
        idx += m
        matrix.append(row)
    
    # Преобразуем в множества защищенных тактик для каждой защиты
    defense_sets = []
    for i in range(n):
        protected = set()
        for j in range(m):
            if matrix[i][j] == 1:
                protected.add(j)
        defense_sets.append(protected)
    
    # Проверяем, есть ли непобедимая защита (защищает от всех атак)
    for protected in defense_sets:
        if len(protected) == m:
            print("Impossible")
            return
    
    # Ищем минимальный набор атак, который покрывает все защиты
    best_attacks = None
    min_size = m + 1
    
    # Перебираем все возможные комбинации атак
    for mask in range(1, 1 << m):
        attacks = set()
        for j in range(m):
            if mask & (1 << j):
                attacks.add(j)
        
        # Проверяем, покрывает ли этот набор все защиты
        covers_all = True
        for protected in defense_sets:
            if attacks.isdisjoint(protected):
                # Эта защита не защищена от нашего набора атак
                continue
            else:
                covers_all = False
                break
        
        if covers_all and len(attacks) < min_size:
            min_size = len(attacks)
            best_attacks = sorted(attacks)
    
    if best_attacks is None:
        print("Impossible")
    else:
        print(str(min_size) + " " + " ".join(str(x + 1) for x in best_attacks))

if __name__ == "__main__":
    main()
