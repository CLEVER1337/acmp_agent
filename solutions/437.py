
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    K = int(data[0])
    N = int(data[1])
    M = int(data[2])
    
    total_players = 2 * K
    agreements = {}
    index = 3
    
    for i in range(N):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        if x not in agreements:
            agreements[x] = set()
        agreements[x].add(y)
    
    candidates = list(map(int, data[index:index+M]))
    index += M
    
    rounds = [0] * (total_players + 1)
    
    for candidate in candidates:
        max_round = 0
        visited = [False] * (total_players + 1)
        visited[candidate] = True
        
        for r in range(1, K + 1):
            players_in_round = total_players // (2 ** (r - 1))
            start_segment = 1
            found = False
            
            while start_segment <= total_players:
                end_segment = start_segment + players_in_round - 1
                
                if start_segment <= candidate <= end_segment:
                    can_win_segment = True
                    
                    for player in range(start_segment, end_segment + 1):
                        if player != candidate and visited[player]:
                            if candidate in agreements.get(player, set()):
                                can_win_segment = False
                                break
                    
                    if can_win_segment:
                        max_round = r
                        for player in range(start_segment, end_segment + 1):
                            visited[player] = True
                        found = True
                        break
                
                start_segment += players_in_round
            
            if not found:
                break
        
        rounds[candidate] = max_round
    
    result = [rounds[c] for c in candidates]
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
