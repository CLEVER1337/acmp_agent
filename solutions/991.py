
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        for i in range(n-1):
            print(0)
        return
            
    clients = [set() for _ in range(n+1)]
    clients[1] = set(range(1, k+1))
    
    rounds = [0] * (n+1)
    received_from = [dict() for _ in range(n+1)]
    upload_count = [0] * (n+1)
    
    current_round = 0
    completed = 1
    
    while completed < n:
        current_round += 1
        
        requests = {}
        for i in range(1, n+1):
            if len(clients[i]) < k:
                available_fragments = set(range(1, k+1)) - clients[i]
                fragment_counts = {}
                for frag in available_fragments:
                    count = sum(1 for j in range(1, n+1) if frag in clients[j])
                    fragment_counts[frag] = count
                
                min_count = min(fragment_counts.values())
                candidate_frags = [frag for frag in fragment_counts if fragment_counts[frag] == min_count]
                chosen_frag = min(candidate_frags)
                
                providers = [j for j in range(1, n+1) if chosen_frag in clients[j] and j != i]
                if providers:
                    provider_uploads = [upload_count[j] for j in providers]
                    min_uploads = min(provider_uploads)
                    candidate_providers = [j for j in providers if upload_count[j] == min_uploads]
                    chosen_provider = min(candidate_providers)
                    
                    if chosen_provider not in requests:
                        requests[chosen_provider] = []
                    requests[chosen_provider].append((i, chosen_frag))
        
        satisfied_requests = []
        for provider, req_list in requests.items():
            if not req_list:
                continue
                
            best_requests = []
            for req in req_list:
                requester, frag = req
                value = received_from[provider].get(requester, 0)
                best_requests.append((value, -len(clients[requester]), -requester, requester, frag))
            
            best_requests.sort(reverse=True)
            best_request = best_requests[0]
            satisfied_requests.append((best_request[3], best_request[4], provider))
            upload_count[provider] += 1
        
        for requester, frag, provider in satisfied_requests:
            clients[requester].add(frag)
            if requester not in received_from[provider]:
                received_from[provider][requester] = 0
            received_from[provider][requester] += 1
            
            if len(clients[requester]) == k and rounds[requester] == 0:
                rounds[requester] = current_round
                completed += 1
    
    for i in range(2, n+1):
        print(rounds[i])

if __name__ == "__main__":
    main()
