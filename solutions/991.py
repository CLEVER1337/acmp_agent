
def main():
    import sys
    n, k = map(int, sys.stdin.readline().split())
    if k == 0:
        for i in range(n-1):
            print(0)
        return
            
    clients = [set() for _ in range(n+1)]
    clients[1] = set(range(1, k+1))
    rounds = [0] * (n+1)
    completed = [False] * (n+1)
    completed[1] = True
    received_from = [[0]*(n+1) for _ in range(n+1)]
    
    time = 0
    while True:
        time += 1
        all_done = True
        for i in range(2, n+1):
            if not completed[i]:
                all_done = False
                break
        if all_done:
            break
            
        requests = {}
        for i in range(2, n+1):
            if completed[i]:
                continue
            available_frags = clients[i]
            needed_frags = set(range(1, k+1)) - available_frags
            if not needed_frags:
                completed[i] = True
                rounds[i] = time - 1
                continue
                
            frag_count = {}
            for frag in needed_frags:
                count = 0
                for j in range(1, n+1):
                    if frag in clients[j]:
                        count += 1
                frag_count[frag] = count
                
            min_count = min(frag_count.values()) if frag_count else float('inf')
            candidate_frags = [frag for frag, cnt in frag_count.items() if cnt == min_count]
            chosen_frag = min(candidate_frags) if candidate_frags else None
            
            if chosen_frag is None:
                continue
                
            possible_sources = []
            for j in range(1, n+1):
                if chosen_frag in clients[j]:
                    upload_count = sum(1 for reqs in requests.values() if reqs and reqs[0] == j)
                    possible_sources.append((len(clients[j]), upload_count, j))
                    
            if not possible_sources:
                continue
                
            possible_sources.sort(key=lambda x: (x[0], x[1], x[2]))
            chosen_source = possible_sources[0][2]
            
            if chosen_source not in requests:
                requests[chosen_source] = []
            requests[chosen_source].append((received_from[i][chosen_source], len(clients[i]), i, chosen_frag))
            
        for source in requests:
            req_list = requests[source]
            req_list.sort(key=lambda x: (-x[0], x[1], x[2]))
            if req_list:
                _, _, client_id, frag = req_list[0]
                clients[client_id].add(frag)
                received_from[client_id][source] += 1
                
        for i in range(2, n+1):
            if len(clients[i]) == k and not completed[i]:
                completed[i] = True
                rounds[i] = time
                
    for i in range(2, n+1):
        print(rounds[i])

if __name__ == "__main__":
    main()
