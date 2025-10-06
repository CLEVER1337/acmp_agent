
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    capacities = list(map(int, data[2:2+n]))
    goods = []
    index = 2 + n
    for i in range(m):
        s = int(data[index])
        a = int(data[index+1])
        d = int(data[index+2])
        index += 3
        goods.append((s, a, d, i))
    
    compartments = [[] for _ in range(n)]
    free_space = capacities[:]
    events = []
    
    for s, a, d, idx in goods:
        events.append((a, 'arrive', s, d, idx))
        events.append((d, 'depart', s, d, idx))
    
    events.sort(key=lambda x: (x[0], 0 if x[1] == 'depart' else 1))
    
    current_goods = {}
    
    for time, event_type, s, d, idx in events:
        if event_type == 'depart':
            for comp_id in range(n):
                for i, (good_s, good_d, good_idx) in enumerate(compartments[comp_id]):
                    if good_idx == idx:
                        compartments[comp_id].pop(i)
                        free_space[comp_id] += good_s
                        print(f"{idx+1} out {comp_id+1}")
                        break
        else:
            best_comp = -1
            min_free = float('inf')
            for comp_id in range(n):
                if free_space[comp_id] >= s:
                    if free_space[comp_id] < min_free:
                        min_free = free_space[comp_id]
                        best_comp = comp_id
            
            if best_comp != -1:
                compartments[best_comp].append((s, d, idx))
                free_space[best_comp] -= s
                print(f"{idx+1} in {best_comp+1}")
                continue
            
            best_move = None
            best_move_size = float('inf')
            best_src_free_after = -float('inf')
            best_dst_free_after = -float('inf')
            best_good_idx = float('inf')
            best_dst_comp = float('inf')
            
            for src_comp in range(n):
                for good_index_in_comp, (good_s, good_d, good_idx) in enumerate(compartments[src_comp]):
                    for dst_comp in range(n):
                        if src_comp == dst_comp:
                            continue
                        if free_space[dst_comp] >= good_s:
                            if free_space[src_comp] + good_s >= s:
                                src_free_after = free_space[src_comp] + good_s - s
                                dst_free_after = free_space[dst_comp] - good_s
                                
                                if best_move is None:
                                    best_move = (src_comp, good_index_in_comp, dst_comp, good_idx, good_s)
                                    best_move_size = good_s
                                    best_src_free_after = src_free_after
                                    best_dst_free_after = dst_free_after
                                    best_good_idx = good_idx
                                    best_dst_comp = dst_comp
                                    continue
                                
                                if good_s < best_move_size:
                                    best_move = (src_comp, good_index_in_comp, dst_comp, good_idx, good_s)
                                    best_move_size = good_s
                                    best_src_free_after = src_free_after
                                    best_dst_free_after = dst_free_after
                                    best_good_idx = good_idx
                                    best_dst_comp = dst_comp
                                    continue
                                
                                if good_s == best_move_size:
                                    if src_free_after < best_src_free_after:
                                        best_move = (src_comp, good_index_in_comp, dst_comp, good_idx, good_s)
                                        best_move_size = good_s
                                        best_src_free_after = src_free_after
                                        best_dst_free_after = dst_free_after
                                        best_good_idx = good_idx
                                        best_dst_comp = dst_comp
                                        continue
                                    
                                    if src_free_after == best_src_free_after:
                                        if dst_free_after < best_dst_free_after:
                                            best_move = (src_comp, good_index_in_comp, dst_comp, good_idx, good_s)
                                            best_move_size = good_s
                                            best_src_free_after = src_free_after
                                            best_dst_free_after = dst_free_after
                                            best_good_idx = good_idx
                                            best_dst_comp = dst_comp
                                            continue
                                        
                                        if dst_free_after == best_dst_free_after:
                                            if good_idx < best_good_idx:
                                                best_move = (src_comp, good_index_in_comp, dst_comp, good_idx, good_s)
                                                best_move_size = good_s
                                                best_src_free_after = src_free_after
                                                best_dst_free_after = dst_free_after
                                                best_good_idx = good_idx
                                                best_dst_comp = dst_comp
                                                continue
                                            
                                            if good_idx == best_good_idx and dst_comp < best_dst_comp:
                                                best_move = (src_comp, good_index_in_comp, dst_comp, good_idx, good_s)
                                                best_move_size = good_s
                                                best_src_free_after = src_free_after
                                                best_dst_free_after = dst_free_after
                                                best_good_idx = good_idx
                                                best_dst_comp = dst_comp
            
            if best_move is None:
                print(f"{idx+1} reject")
            else:
                src_comp, good_index, dst_comp, move_good_idx, move_good_s = best_move
                move_good_s, move_good_d, _ = compartments[src_comp][good_index]
                
                compartments[src_comp].pop(good_index)
                free_space[src_comp] += move_good_s
                print(f"{move_good_idx+1} out {src_comp+1}")
                
                compartments[dst_comp].append((move_good_s, move_good_d, move_good_idx))
                free_space[dst_comp] -= move_good_s
                print(f"{move_good_idx+1} in {dst_comp+1}")
                
                compartments[src_comp].append((s, d, idx))
                free_space[src_comp] -= s
                print(f"{idx+1} in {src_comp+1}")

if __name__ == "__main__":
    main()
