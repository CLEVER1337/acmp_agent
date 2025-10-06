
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, r = map(int, data[0].split())
    word = data[1].strip()
    q_list = list(map(float, data[2].split()))
    
    L = len(word)
    unique_letters = set(word)
    m = len(unique_letters)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(mask, turn, i, j, k):
        if k == 0:
            return 1.0 if turn == r - 1 else 0.0
        
        total_prob = 0.0
        current_player = turn % n
        q = q_list[current_player]
        
        found = False
        for idx, char in enumerate(word):
            if mask & (1 << idx):
                continue
            if char in guessed:
                continue
            
            if char not in guessed:
                guessed.add(char)
                new_mask = mask
                count = 0
                for pos, c in enumerate(word):
                    if c == char:
                        new_mask |= (1 << pos)
                        count += 1
                new_k = k - count
                new_i = i - 1
                new_j = j - 1
                
                prob_correct = (1.0 / j) * (1 - (1 - q) ** i)
                result = dp(new_mask, turn, new_i, new_j, new_k)
                total_prob += prob_correct * result
                
                guessed.remove(char)
                found = True
        
        if not found:
            for char in unique_letters:
                if char not in guessed:
                    guessed.add(char)
                    new_mask = mask
                    count = 0
                    for pos, c in enumerate(word):
                        if c == char:
                            new_mask |= (1 << pos)
                            count += 1
                    new_k = k - count
                    new_i = i - 1
                    new_j = j - 1
                    
                    prob_correct = (1.0 / j) * (1 - (1 - q) ** i)
                    result = dp(new_mask, turn, new_i, new_j, new_k)
                    total_prob += prob_correct * result
                    
                    guessed.remove(char)
        
        prob_wrong = 1 - (1 - (1 - q) ** i)
        next_turn = (turn + 1) % n
        total_prob += prob_wrong * dp(mask, next_turn, i, j, k)
        
        return total_prob

    guessed = set()
    initial_mask = 0
    initial_i = m
    initial_j = m
    initial_k = L
    
    result = dp(initial_mask, 0, initial_i, initial_j, initial_k)
    print("{:.15f}".format(result))

if __name__ == "__main__":
    main()
