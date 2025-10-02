
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    if n == 1:
        print("1")
        print(arr[0])
        return
        
    arr.sort()
    
    def can_form_ap_with_d(selected, d):
        if len(selected) == 0:
            return True
        if len(selected) == 1:
            return True
            
        selected_sorted = sorted(selected)
        for i in range(1, len(selected_sorted)):
            if (selected_sorted[i] - selected_sorted[i-1]) % d != 0:
                return False
        return True
        
    def is_winning_state(remaining, current_set):
        if len(remaining) == 0:
            return False
            
        for i in range(len(remaining)):
            new_remaining = remaining[:i] + remaining[i+1:]
            new_set = current_set + [remaining[i]]
            
            found_valid_d = False
            for d in range(2, 100001):
                if can_form_ap_with_d(new_set, d):
                    if not is_winning_state(new_remaining, new_set):
                        return True
                    found_valid_d = True
                    break
                    
            if not found_valid_d:
                continue
                
        return False
        
    winning_moves = []
    for i in range(len(arr)):
        first_move = arr[i]
        remaining = arr[:i] + arr[i+1:]
        current_set = [first_move]
        
        found_valid_d = False
        for d in range(2, 100001):
            if can_form_ap_with_d(current_set, d):
                if not is_winning_state(remaining, current_set):
                    winning_moves.append(first_move)
                    found_valid_d = True
                    break
                    
    winning_moves = sorted(list(set(winning_moves)))
    print(str(len(winning_moves)))
    if winning_moves:
        print(" ".join(map(str, winning_moves)))
    else:
        print()

if __name__ == "__main__":
    main()
