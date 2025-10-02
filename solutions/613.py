
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, r = map(int, data[0].split())
    word = data[1].strip()
    q = list(map(float, data[2].split()))
    
    L = len(word)
    unique_letters = set(word)
    k = len(unique_letters)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(mask, turn):
        closed_count = bin(mask).count('1')
        if closed_count == 0:
            return 1.0 if turn == 0 else 0.0
        
        unknown_letters = set()
        letter_positions = {}
        for i in range(L):
            if mask & (1 << i):
                letter = word[i]
                if letter not in letter_positions:
                    letter_positions[letter] = []
                letter_positions[letter].append(i)
                unknown_letters.add(letter)
        
        j = len(unknown_letters)
        current_player = turn % n
        prob_correct = q[current_player]
        
        if j == 0:
            return 1.0 if turn == 0 else 0.0
        
        prob_win = 0.0
        
        for letter in unknown_letters:
            new_mask = mask
            for pos in letter_positions[letter]:
                new_mask &= ~(1 << pos)
            
            p_letter = 1.0 / j
            p_guess = prob_correct * p_letter
            
            if new_mask == mask:
                next_turn = (turn + 1) % n
                result = dp(new_mask, next_turn)
            else:
                result = dp(new_mask, turn)
            
            prob_win += p_guess * result
        
        prob_wrong = 1.0 - prob_correct
        if prob_wrong > 1e-12:
            next_turn = (turn + 1) % n
            prob_win += prob_wrong * dp(mask, next_turn)
        
        return prob_win
    
    initial_mask = (1 << L) - 1
    result = dp(initial_mask, 0)
    print("{:.15f}".format(result))

if __name__ == "__main__":
    main()
