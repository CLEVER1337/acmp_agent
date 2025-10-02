
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    W = int(data[1])
    items = []
    index = 2
    for i in range(n):
        w = int(data[index])
        p = int(data[index+1])
        index += 2
        items.append((w, p, i+1))
    
    max_profit = 0
    best_mask = 0
    min_items = float('inf')
    
    for mask in range(1, 1 << n):
        total_weight = 0
        total_profit = 0
        count = 0
        for i in range(n):
            if mask & (1 << i):
                total_weight += items[i][0]
                total_profit += items[i][1]
                count += 1
                if total_weight > W:
                    break
        
        if total_weight <= W:
            if total_profit > max_profit:
                max_profit = total_profit
                best_mask = mask
                min_items = count
            elif total_profit == max_profit:
                if count < min_items:
                    best_mask = mask
                    min_items = count
                elif count == min_items:
                    for i in range(n):
                        bit1 = (best_mask >> i) & 1
                        bit2 = (mask >> i) & 1
                        if bit1 != bit2:
                            if bit2 < bit1:
                                best_mask = mask
                            break
    
    selected_indices = []
    count_selected = 0
    for i in range(n):
        if best_mask & (1 << i):
            selected_indices.append(items[i][2])
            count_selected += 1
    
    print(f"{count_selected} {max_profit}")
    print(" ".join(map(str, sorted(selected_indices))))

if __name__ == "__main__":
    main()
