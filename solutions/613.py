
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    n, r = map(int, data[0].split())
    word = data[1].strip()
    q = list(map(float, data[2].split()))
    
    length = len(word)
    unique_letters = set(word)
    letter_count = defaultdict(int)
    for c in word:
        letter_count[c] += 1
    
    total_states = 1 << length
    dp = [[0.0] * total_states for _ in range(n)]
    
    for state in range(total_states - 1, -1, -1):
        open_count = bin(state).count('1')
        if open_count == length:
            for i in range(n):
                dp[i][state] = 1.0 if i == 0 else 0.0
            continue
            
        closed_positions = []
        closed_letters = set()
        for pos in range(length):
            if not (state & (1 << pos)):
                closed_positions.append(pos)
                closed_letters.add(word[pos])
                
        k = len(closed_positions)
        j = len(closed_letters)
        remaining_letters = sorted(closed_letters)
        
        for player_idx in range(n):
            total_prob = 0.0
            current_q = q[player_idx]
            
            prob_correct = current_q * (1.0 / j) if j > 0 else 0.0
            prob_wrong = (1.0 - current_q) if j > 0 else 1.0
            
            if j == 0:
                next_player = (player_idx + 1) % n
                total_prob += dp[next_player][state]
            else:
                for letter in remaining_letters:
                    new_state = state
                    count_found = 0
                    for pos in closed_positions:
                        if word[pos] == letter:
                            new_state |= (1 << pos)
                            count_found += 1
                    
                    if count_found > 0:
                        total_prob += prob_correct * dp[player_idx][new_state]
                    else:
                        next_player = (player_idx + 1) % n
                        total_prob += prob_correct * dp[next_player][new_state]
                
                next_player = (player_idx + 1) % n
                total_prob += prob_wrong * dp[next_player][state]
                
            dp[player_idx][state] = total_prob
            
    initial_state = 0
    result = dp[r - 1][initial_state]
    print("{:.15f}".format(result))

if __name__ == "__main__":
    main()
