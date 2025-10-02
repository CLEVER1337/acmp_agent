
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0]); m = int(data[1])
    capacities = list(map(int, data[2:2+n]))
    goods = []
    index = 2 + n
    for i in range(m):
        s = int(data[index]); a = int(data[index+1]); d = int(data[index+2])
        index += 3
        goods.append((s, a, d, i))
    
    compartments = [[] for _ in range(n)]
    free_space = capacities[:]
    events = []
    
    for s, a, d, idx in goods:
        events.append((a, 'arrive', idx))
        events.append((d, 'depart', idx))
    
    events.sort(key=lambda x: (x[0], 0 if x[1] == 'arrive' else 1))
    
    current_goods_in_compartment = {}
    
    for time, event_type, idx in events:
        if event_type == 'arrive':
            s, a, d, _ = goods[idx]
            best_comp = -1
            min_free = float('inf')
            for i in range(n):
                if free_space[i] >= s:
                    if free_space[i] < min_free:
                        min_free = free_space[i]
                        best_comp = i
            if best_comp != -1:
                compartments[best_comp].append((s, idx))
                free_space[best_comp] -= s
                current_goods_in_compartment[idx] = best_comp
                print(f"put cargo {idx+1} to compartment {best_comp+1}")
            else:
                found = False
                best_move = None
                best_move_size = float('inf')
                best_source_free_after = -1
                best_target_free_after = float('inf')
                best_cargo_idx = float('inf')
                best_target_comp = float('inf')
                
                for source_comp in range(n):
                    if not compartments[source_comp]:
                        continue
                    for cargo_idx_in_source in range(len(compartments[source_comp])):
                        cargo_size, cargo_id = compartments[source_comp][cargo_idx_in_source]
                        for target_comp in range(n):
                            if target_comp == source_comp:
                                continue
                            if free_space[target_comp] >= cargo_size:
                                if free_space[source_comp] + cargo_size >= s:
                                    source_free_after = free_space[source_comp] + cargo_size - s
                                    target_free_after = free_space[target_comp] - cargo_size
                                    if best_move is None:
                                        best_move = (source_comp, cargo_idx_in_source, target_comp, cargo_id)
                                        best_move_size = cargo_size
                                        best_source_free_after = source_free_after
                                        best_target_free_after = target_free_after
                                        best_cargo_idx = cargo_id
                                        best_target_comp = target_comp
                                    else:
                                        if cargo_size < best_move_size:
                                            best_move = (source_comp, cargo_idx_in_source, target_comp, cargo_id)
                                            best_move_size = cargo_size
                                            best_source_free_after = source_free_after
                                            best_target_free_after = target_free_after
                                            best_cargo_idx = cargo_id
                                            best_target_comp = target_comp
                                        elif cargo_size == best_move_size:
                                            if source_free_after < best_source_free_after:
                                                best_move = (source_comp, cargo_idx_in_source, target_comp, cargo_id)
                                                best_move_size = cargo_size
                                                best_source_free_after = source_free_after
                                                best_target_free_after = target_free_after
                                                best_cargo_idx = cargo_id
                                                best_target_comp = target_comp
                                            elif source_free_after == best_source_free_after:
                                                if target_free_after < best_target_free_after:
                                                    best_move = (source_comp, cargo_idx_in_source, target_comp, cargo_id)
                                                    best_move_size = cargo_size
                                                    best_source_free_after = source_free_after
                                                    best_target_free_after = target_free_after
                                                    best_cargo_idx = cargo_id
                                                    best_target_comp = target_comp
                                                elif target_free_after == best_target_free_after:
                                                    if cargo_id < best_cargo_idx:
                                                        best_move = (source_comp, cargo_idx_in_source, target_comp, cargo_id)
                                                        best_move_size = cargo_size
                                                        best_source_free_after = source_free_after
                                                        best_target_free_after = target_free_after
                                                        best_cargo_idx = cargo_id
                                                        best_target_comp = target_comp
                                                    elif cargo_id == best_cargo_idx and target_comp < best_target_comp:
                                                        best_move = (source_comp, cargo_idx_in_source, target_comp, cargo_id)
                                                        best_move_size = cargo_size
                                                        best_source_free_after = source_free_after
                                                        best_target_free_after = target_free_after
                                                        best_cargo_idx = cargo_id
                                                        best_target_comp = target_comp
                
                if best_move is not None:
                    source_comp, cargo_idx_in_source, target_comp, cargo_id = best_move
                    cargo_size = compartments[source_comp][cargo_idx_in_source][0]
                    
                    compartments[target_comp].append(compartments[source_comp][cargo_idx_in_source])
                    free_space[target_comp] -= cargo_size
                    del compartments[source_comp][cargo_idx_in_source]
                    free_space[source_comp] += cargo_size
                    
                    compartments[source_comp].append((s, idx))
                    free_space[source_comp] -= s
                    current_goods_in_compartment[idx] = source_comp
                    current_goods_in_compartment[cargo_id] = target_comp
                    
                    print(f"move cargo {cargo_id+1} from compartment {source_comp+1} to compartment {target_comp+1}")
                    print(f"put cargo {idx+1} to compartment {source_comp+1}")
                    found = True
                
                if not found:
                    print(f"reject cargo {idx+1}")
        else:
            if idx in current_goods_in_compartment:
                comp = current_goods_in_compartment[idx]
                s = goods[idx][0]
                for i in range(len(compartments[comp])):
                    if compartments[comp][i][1] == idx:
                        del compartments[comp][i]
                        free_space[comp] += s
                        break
                del current_goods_in_compartment[idx]
                print(f"remove cargo {idx+1} from compartment {comp+1}")

if __name__ == "__main__":
    main()
