
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("Crisis")
        return
        
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    preferences = []
    index = 3
    for i in range(n):
        row = list(map(int, data[index:index+k]))
        preferences.append(row)
        index += k
    
    # Создаем обратное отображение: для каждого депутата и каждого законопроекта - его позиция в предпочтениях
    rank = [[0] * (k + 1) for _ in range(n)]
    for i in range(n):
        for pos, bill in enumerate(preferences[i]):
            rank[i][bill] = pos + 1  # позиция от 1 до k
    
    # Функция для проверки, может ли законопроект x быть принят
    def can_pass(x):
        # Для каждого депутата определяем, будет ли он голосовать за x
        votes = 0
        for i in range(n):
            # Если законопроект x предпочтительнее для депутата i, чем кризис (т.е. имеет ранг лучше чем k+1)
            # и при этом x предпочтительнее, чем любой законопроект с номером < x, который может быть принят?
            # Но это сложно, поэтому используем другой подход: депутат будет голосовать за x, если:
            # 1. x находится в его списке предпочтений ДО любого законопроекта с номером < x, который может быть принят
            # 2. Или если таких законопроектов нет, то за x
            
            # Найдем минимальный ранг среди законопроектов с номерами < x
            min_rank_before = k + 1
            for j in range(1, x):
                if rank[i][j] > 0 and rank[i][j] < min_rank_before:
                    min_rank_before = rank[i][j]
            
            # Если x имеет лучший ранг, чем минимальный ранг законопроектов до x, то депутат предпочтет x
            if rank[i][x] > 0 and (min_rank_before == k + 1 or rank[i][x] < min_rank_before):
                votes += 1
            else:
                # Проверим, может ли депутат быть вынужден голосовать за x, чтобы избежать кризиса
                # Если все законопроекты с номерами < x отвергнуты, и x - лучший вариант для избежания кризиса
                min_rank_after = k + 1
                for j in range(x, k + 1):
                    if rank[i][j] > 0 and rank[i][j] < min_rank_after:
                        min_rank_after = rank[i][j]
                
                if min_rank_after == rank[i][x]:
                    votes += 1
        
        return votes >= m
    
    # Проверяем законопроекты по порядку от 1 до k
    for x in range(1, k + 1):
        if can_pass(x):
            print(x)
            return
    
    print("Crisis")

if __name__ == "__main__":
    main()
