
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    participants = []
    for i in range(n):
        a = float(data[1 + 2*i])
        b = float(data[2 + 2*i])
        participants.append((a, b))
    
    can_win = []
    for idx in range(n):
        a0, b0 = participants[idx]
        max_possible_total = a0 + b0
        possible = True
        
        for j in range(n):
            if j == idx:
                continue
                
            aj, bj = participants[j]
            min_needed_total = max_possible_total
            
            max_aj = min(100, aj + (100 - aj))
            max_bj = min(100, bj + (100 - bj))
            max_total_j = max_aj + max_bj
            
            if max_total_j < min_needed_total:
                possible = False
                break
                
        if possible:
            can_win.append(idx + 1)
            
    print(f"{len(can_win)}")
    if can_win:
        print(" ".join(map(str, can_win)))
    else:
        print()

if __name__ == "__main__":
    main()
