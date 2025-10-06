
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    K = int(data[0])
    N = int(data[1])
    M = int(data[2])
    total_players = 1 << K
    
    agreements = {}
    index = 3
    for i in range(N):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        agreements[(min(x, y), max(x, y))] = x
    
    candidates = list(map(int, data[index:index+M]))
    index += M
    
    rounds = [0] * (total_players + 1)
    
    def can_win_in_round(player, round_num):
        if round_num == 0:
            return True
            
        start_segment = ((player - 1) >> (round_num - 1)) << (round_num - 1)
        segment_size = 1 << (round_num - 1)
        left_segment = start_segment + 1
        right_segment = start_segment + segment_size
        opponent_segment_start = left_segment if player > right_segment else right_segment + 1
        opponent_segment_end = opponent_segment_start + segment_size - 1
        
        for opp in range(opponent_segment_start, opponent_segment_end + 1):
            if opp < 1 or opp > total_players:
                continue
                
            key = (min(player, opp), max(player, opp))
            if key in agreements:
                if agreements[key] != player:
                    return False
            else:
                pass
                
        return True
        
    for player in range(1, total_players + 1):
        max_round = 0
        for r in range(1, K + 1):
            if can_win_in_round(player, r):
                max_round = r
            else:
                break
        rounds[player] = max_round
        
    result = []
    for cand in candidates:
        result.append(str(rounds[cand]))
        
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
