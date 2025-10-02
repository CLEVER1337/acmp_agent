
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    K = int(data[0])
    N = int(data[1])
    M = int(data[2])
    total_players = 2 * K
    
    agreements = defaultdict(set)
    idx = 3
    for i in range(N):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        agreements[x].add(y)
    
    candidates = list(map(int, data[idx:idx+M]))
    idx += M
    
    rounds = [0] * (total_players + 1)
    
    for player in range(1, total_players + 1):
        can_win = [False] * (total_players + 1)
        can_win[player] = True
        
        for round_num in range(1, K + 1):
            next_can_win = [False] * (total_players + 1)
            matches = total_players // (2 ** (round_num - 1))
            
            for match in range(matches // 2):
                left_start = 2 * match * (2 ** (round_num - 1)) + 1
                right_start = left_start + (2 ** (round_num - 1))
                
                for left in range(left_start, left_start + (2 ** (round_num - 1))):
                    if not can_win[left]:
                        continue
                    for right in range(right_start, right_start + (2 ** (round_num - 1))):
                        if not can_win[right]:
                            continue
                            
                        if right in agreements.get(left, set()):
                            next_can_win[left] = True
                        elif left in agreements.get(right, set()):
                            next_can_win[right] = True
                        else:
                            next_can_win[left] = True
                            next_can_win[right] = True
                
            if any(next_can_win):
                can_win = next_can_win
                rounds[player] = round_num
            else:
                break
    
    result = []
    for candidate in candidates:
        result.append(str(rounds[candidate]))
    
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
