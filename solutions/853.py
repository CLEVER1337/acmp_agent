
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
        nums = sorted(selected)
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) % d != 0:
                return False
        return True
    
    def get_possible_d(selected):
        nums = sorted(selected)
        if len(nums) == 1:
            return set(range(2, max(arr) + 1))
            
        possible_d = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = abs(nums[j] - nums[i])
                if diff == 0:
                    continue
                for divisor in range(2, diff + 1):
                    if diff % divisor == 0:
                        d = divisor
                        if can_form_ap(selected, d):
                            possible_d.add(d)
        return possible_d
    
    winning_moves = []
    
    for first_move in arr:
        remaining = arr.copy()
        remaining.remove(first_move)
        selected = [first_move]
        
        def can_win(selected, remaining, player_turn):
            if not remaining:
                return player_turn == 1
                
            possible_d = get_possible_d(selected)
            if not possible_d:
                return player_turn == 1
                
            if player_turn == 0:
                for next_move in remaining:
                    new_selected = selected + [next_move]
                    new_remaining = remaining.copy()
                    new_remaining.remove(next_move)
                    
                    new_possible_d = get_possible_d(new_selected)
                    if not new_possible_d:
                        continue
                        
                    if not can_win(new_selected, new_remaining, 1):
                        return False
                return True
            else:
                for next_move in remaining:
                    new_selected = selected + [next_move]
                    new_remaining = remaining.copy()
                    new_remaining.remove(next_move)
                    
                    new_possible_d = get_possible_d(new_selected)
                    if not new_possible_d:
                        return True
                        
                    if can_win(new_selected, new_remaining, 0):
                        return True
                return False
        
        if can_win(selected, remaining, 0):
            winning_moves.append(first_move)
    
    winning_moves.sort()
    print(len(winning_moves))
    if winning_moves:
        print(" ".join(map(str, winning_moves)))
    else:
        print()

if __name__ == "__main__":
    main()
