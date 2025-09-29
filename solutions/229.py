
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    participants = []
    index = 1
    for i in range(n):
        a = float(data[index])
        b = float(data[index + 1])
        index += 2
        participants.append((a, b, i + 1))
    
    possible_winners = []
    
    for i in range(n):
        a_i, b_i, idx_i = participants[i]
        max_total = a_i + b_i
        
        can_win = True
        
        for j in range(n):
            if i == j:
                continue
                
            a_j, b_j, idx_j = participants[j]
            current_total_j = a_j + b_j
            
            if current_total_j <= max_total:
                continue
                
            max_possible_j = min(100, a_j) + min(100, b_j)
            if max_possible_j > max_total:
                can_win = False
                break
                
        if can_win:
            possible_winners.append(idx_i)
    
    possible_winners.sort()
    print(f"{len(possible_winners)}")
    if possible_winners:
        print(" ".join(map(str, possible_winners)))
    else:
        print()

if __name__ == "__main__":
    main()
