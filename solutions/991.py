
def main():
    with open('INPUT.TXT', 'r') as f:
        n, k = map(int, f.read().split())
    
    if k == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('')
        return
    
    clients = [set() for _ in range(n)]
    clients[0] = set(range(1, k+1))
    rounds = [0] * n
    received_from = [[0] * n for _ in range(n)]
    current_round = 0
    
    while any(len(client) < k for client in clients):
        current_round += 1
        requests = []
        providers_requests = [[] for _ in range(n)]
        
        for i in range(n):
            if len(clients[i]) == k:
                continue
                
            available_frags = clients[i]
            needed_frags = set(range(1, k+1)) - available_frags
            
            frag_counts = {}
            for frag in needed_frags:
                count = sum(1 for client in clients if frag in client)
                frag_counts[frag] = count
            
            if not frag_counts:
                continue
                
            min_count = min(frag_counts.values())
            candidate_frags = [frag for frag, count in frag_counts.items() if count == min_count]
            chosen_frag = min(candidate_frags)
            
            possible_providers = []
            for j in range(n):
                if i != j and chosen_frag in clients[j]:
                    upload_count = sum(1 for req in providers_requests[j] if req is not None)
                    possible_providers.append((upload_count, j))
            
            if not possible_providers:
                requests.append((i, None, chosen_frag))
                continue
                
            min_upload_count = min(prov[0] for prov in possible_providers)
            candidate_providers = [j for upload_count, j in possible_providers if upload_count == min_upload_count]
            chosen_provider = min(candidate_providers)
            
            requests.append((i, chosen_provider, chosen_frag))
            providers_requests[chosen_provider].append(i)
        
        satisfied = set()
        for provider in range(n):
            if not providers_requests[provider]:
                continue
                
            requests_to_provider = providers_requests[provider]
            if not requests_to_provider:
                continue
                
            request_metrics = []
            for requester in requests_to_provider:
                value = received_from[provider][requester]
                frag_count = len(clients[requester])
                request_metrics.append((value, frag_count, requester))
            
            request_metrics.sort(key=lambda x: (-x[0], x[1], x[2]))
            satisfied_requester = request_metrics[0][2]
            satisfied.add((satisfied_requester, provider))
        
        for i, provider, frag in requests:
            if provider is None:
                continue
            if (i, provider) in satisfied:
                clients[i].add(frag)
                received_from[i][provider] += 1
                if len(clients[i]) == k and rounds[i] == 0:
                    rounds[i] = current_round
    
    with open('OUTPUT.TXT', 'w') as f:
        for i in range(1, n):
            f.write(f"{rounds[i]}\n")

if __name__ == "__main__":
    main()
