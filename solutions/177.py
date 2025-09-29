
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
    free_space = capacities.copy()
    events = []
    
    for good in goods:
        s, a, d, idx = good
        events.append((a, 'arrive', idx))
        events.append((d, 'depart', idx))
    
    events.sort(key=lambda x: x[0])
    
    good_info = {}
    for idx, (s, a, d, orig_idx) in enumerate(goods):
        good_info[idx] = {'size': s, 'compartment': -1}
    
    def find_compartment_for_good(good_size):
        candidates = []
        for comp_id in range(n):
            if free_space[comp_id] >= good_size:
                candidates.append((free_space[comp_id], comp_id))
        if not candidates:
            return -1
        candidates.sort(key=lambda x: (x[0], x[1]))
        return candidates[0][1]
    
    def find_good_to_move(target_comp, required_space):
        best_option = None
        for comp_from in range(n):
            if comp_from == target_comp:
                continue
            for good_idx_in_comp in compartments[comp_from]:
                good_size = good_info[good_idx_in_comp]['size']
                if free_space[target_comp] + good_size >= required_space:
                    new_free_from = free_space[comp_from] + good_size
                    new_free_to = free_space[target_comp] - good_size
                    option = (good_size, new_free_from, new_free_to, good_idx_in_comp, comp_from, target_comp)
                    if best_option is None:
                        best_option = option
                    else:
                        if good_size < best_option[0]:
                            best_option = option
                        elif good_size == best_option[0]:
                            if new_free_from < best_option[1]:
                                best_option = option
                            elif new_free_from == best_option[1]:
                                if new_free_to < best_option[2]:
                                    best_option = option
                                elif new_free_to == best_option[2]:
                                    if good_idx_in_comp < best_option[3]:
                                        best_option = option
                                    elif good_idx_in_comp == best_option[3]:
                                        if target_comp < best_option[5]:
                                            best_option = option
        return best_option
    
    for time, event_type, good_idx in events:
        if event_type == 'arrive':
            s = goods[good_idx][0]
            comp_id = find_compartment_for_good(s)
            if comp_id != -1:
                free_space[comp_id] -= s
                compartments[comp_id].append(good_idx)
                good_info[good_idx]['compartment'] = comp_id
                print(f"груз {good_idx+1} размещен в отсеке {comp_id+1}")
            else:
                found = False
                best_move_option = None
                for target_comp in range(n):
                    move_option = find_good_to_move(target_comp, s)
                    if move_option:
                        if best_move_option is None:
                            best_move_option = move_option
                        else:
                            g_size, new_f_from, new_f_to, g_idx, comp_from, comp_to = move_option
                            b_g_size, b_new_f_from, b_new_f_to, b_g_idx, b_comp_from, b_comp_to = best_move_option
                            if g_size < b_g_size:
                                best_move_option = move_option
                            elif g_size == b_g_size:
                                if new_f_from < b_new_f_from:
                                    best_move_option = move_option
                                elif new_f_from == b_new_f_from:
                                    if new_f_to < b_new_f_to:
                                        best_move_option = move_option
                                    elif new_f_to == b_new_f_to:
                                        if g_idx < b_g_idx:
                                            best_move_option = move_option
                                        elif g_idx == b_g_idx:
                                            if comp_to < b_comp_to:
                                                best_move_option = move_option
                if best_move_option:
                    g_size, new_f_from, new_f_to, move_good_idx, comp_from, comp_to = best_move_option
                    compartments[comp_from].remove(move_good_idx)
                    free_space[comp_from] += g_size
                    compartments[comp_to].append(move_good_idx)
                    free_space[comp_to] -= g_size
                    good_info[move_good_idx]['compartment'] = comp_to
                    print(f"груз {move_good_idx+1} перемещен из отсека {comp_from+1} в отсек {comp_to+1}")
                    
                    free_space[comp_to] -= s
                    compartments[comp_to].append(good_idx)
                    good_info[good_idx]['compartment'] = comp_to
                    print(f"груз {good_idx+1} размещен в отсеке {comp_to+1}")
                    found = True
                if not found:
                    print(f"груз {good_idx+1} не принят")
        else:
            comp_id = good_info[good_idx]['compartment']
            if comp_id != -1:
                s = good_info[good_idx]['size']
                compartments[comp_id].remove(good_idx)
                free_space[comp_id] += s
                print(f"груз {good_idx+1} забран из отсека {comp_id+1}")

if __name__ == "__main__":
    main()
