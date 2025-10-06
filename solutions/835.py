
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
    
    best_value = -1
    best_mask = 0
    best_count = float('inf')
    
    total = 1 << n
    for mask in range(total):
        total_weight = 0
        total_value = 0
        count = 0
        for i in range(n):
            if mask & (1 << i):
                total_weight += items[i][0]
                total_value += items[i][1]
                count += 1
                if total_weight > W:
                    break
        if total_weight <= W:
            if total_value > best_value:
                best_value = total_value
                best_mask = mask
                best_count = count
            elif total_value == best_value:
                if count < best_count:
                    best_mask = mask
                    best_count = count
                elif count == best_count:
                    current_mask = mask
                    for i in range(n):
                        bit1 = (best_mask >> i) & 1
                        bit2 = (current_mask >> i) & 1
                        if bit1 != bit2:
                            if bit2 < bit1:
                                best_mask = current_mask
                            break
    
    selected = []
    for i in range(n):
        if best_mask & (1 << i):
            selected.append(items[i][2])
    
    selected.sort()
    print(f"{len(selected)} {best_value}")
    if selected:
        print(" ".join(map(str, selected)))
    else:
        print()

if __name__ == "__main__":
    main()
