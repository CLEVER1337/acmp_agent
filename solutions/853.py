
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    if n == 1:
        print(1)
        print(arr[0])
        return
        
    arr.sort()
    
    def can_form_ap(selected, d):
        if len(selected) == 0:
            return True
        if len(selected) == 1:
            return True
            
        min_val = min(selected)
        max_val = max(selected)
        
        if (max_val - min_val) % d != 0:
            return False
            
        step = (max_val - min_val) // d
        if step == 0:
            return len(selected) == 1
            
        for num in selected:
            if (num - min_val) % step != 0:
                return False
                
        return True
        
    def is_winning_state(remaining, current_set, d):
        if len(remaining) == 0:
            return False
            
        for num in remaining:
            new_set = current_set | {num}
            if can_form_ap(new_set, d):
                new_remaining = remaining - {num}
                if not is_winning_move(new_remaining, new_set, d):
                    return True
                    
        return False
        
    def is_winning_move(remaining, current_set, d):
        if len(remaining) == 0:
            return True
            
        for num in remaining:
            new_set = current_set | {num}
            if can_form_ap(new_set, d):
                new_remaining = remaining - {num}
                if not is_winning_state(new_remaining, new_set, d):
                    return True
                    
        return False
        
    winning_moves = []
    s = set(arr)
    
    for first_move in arr:
        remaining = s - {first_move}
        current_set = {first_move}
        
        found_winning = False
        for d in range(2, max(arr) + 1):
            if can_form_ap(current_set, d):
                if not is_winning_state(remaining, current_set, d):
                    found_winning = True
                    break
                    
        if found_winning:
            winning_moves.append(first_move)
            
    winning_moves.sort()
    print(len(winning_moves))
    if winning_moves:
        print(" ".join(map(str, winning_moves)))
    else:
        print()

if __name__ == "__main__":
    main()
