
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
    
    best_value = 0
    best_mask = 0
    best_count = float('inf')
    
    total_states = 1 << n
    for mask in range(total_states):
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
                    current_indices = []
                    new_indices = []
                    for i in range(n):
                        if best_mask & (1 << i):
                            current_indices.append(items[i][2])
                        if mask & (1 << i):
                            new_indices.append(items[i][2])
                    
                    current_indices.sort()
                    new_indices.sort()
                    
                    for curr_idx, new_idx in zip(current_indices, new_indices):
                        if new_idx < curr_idx:
                            best_mask = mask
                            break
                        elif new_idx > curr_idx:
                            break
    
    selected_indices = []
    total_val = 0
    for i in range(n):
        if best_mask & (1 << i):
            selected_indices.append(items[i][2])
            total_val += items[i][1]
    
    selected_indices.sort()
    print(f"{len(selected_indices)} {total_val}")
    print(" ".join(map(str, selected_indices)))

if __name__ == "__main__":
    main()
