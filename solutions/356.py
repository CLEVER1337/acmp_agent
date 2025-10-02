
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    E = int(data[0])
    F = int(data[1])
    total_weight = F - E
    N = int(data[2])
    
    coins = []
    index = 3
    for i in range(N):
        p = int(data[index])
        w = int(data[index+1])
        index += 2
        coins.append((p, w))
    
    INF = float('inf')
    
    # Для минимальной суммы
    dp_min = [INF] * (total_weight + 1)
    dp_min[0] = 0
    
    # Для максимальной суммы
    dp_max = [-INF] * (total_weight + 1)
    dp_max[0] = 0
    
    for i in range(total_weight + 1):
        if dp_min[i] != INF:
            for p, w in coins:
                if i + w <= total_weight:
                    if dp_min[i + w] > dp_min[i] + p:
                        dp_min[i + w] = dp_min[i] + p
        
        if dp_max[i] != -INF:
            for p, w in coins:
                if i + w <= total_weight:
                    if dp_max[i + w] < dp_max[i] + p:
                        dp_max[i + w] = dp_max[i] + p
    
    min_sum = dp_min[total_weight]
    max_sum = dp_max[total_weight]
    
    if min_sum == INF:
        print("This is impossible.")
    else:
        print(f"{min_sum} {max_sum}")

if __name__ == "__main__":
    main()
