
def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    data = lines[0].split()
    N = int(data[0])
    M = int(data[1])
    trump = data[2]
    
    hand = lines[1].split()
    attack = lines[2].split()
    
    ranks = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    def get_rank(card):
        return ranks.index(card[0])
    
    def can_cover(attacking_card, defending_card):
        a_rank, a_suit = attacking_card[0], attacking_card[1]
        d_rank, d_suit = defending_card[0], defending_card[1]
        
        if a_suit == d_suit:
            return get_rank(defending_card) > get_rank(attacking_card)
        elif d_suit == trump:
            return True
        return False
    
    def can_cover_trump(attacking_card, defending_card):
        a_rank, a_suit = attacking_card[0], attacking_card[1]
        d_rank, d_suit = defending_card[0], defending_card[1]
        
        if a_suit == trump:
            return d_suit == trump and get_rank(defending_card) > get_rank(attacking_card)
        return False
    
    from itertools import permutations
    
    hand_copy = hand.copy()
    attack_copy = attack.copy()
    
    if M == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('YES')
        return
    
    for perm in permutations(hand_copy, M):
        valid = True
        used = set()
        
        for i in range(M):
            att_card = attack_copy[i]
            def_card = perm[i]
            
            if def_card in used:
                valid = False
                break
                
            used.add(def_card)
            
            if att_card[1] == trump:
                if not can_cover_trump(att_card, def_card):
                    valid = False
                    break
            else:
                if not can_cover(att_card, def_card):
                    valid = False
                    break
        
        if valid:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('YES')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('NO')

if __name__ == '__main__':
    main()
