
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print("This is impossible.")
        return
        
    E = int(data[0])
    F = int(data[1])
    total_weight = F - E
    n = int(data[2])
    
    coins = []
    index = 3
    for i in range(n):
        p = int(data[index])
        w = int(data[index+1])
        index += 2
        coins.append((p, w))
    
    INF = 10**18
    dp_min = [INF] * (total_weight + 1)
    dp_max = [-INF] * (total_weight + 1)
    dp_min[0] = 0
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
    
    if dp_min[total_weight] == INF:
        print("This is impossible.")
    else:
        print(f"{dp_min[total_weight]} {dp_max[total_weight]}")

if __name__ == "__main__":
    main()
