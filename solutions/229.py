
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    participants = []
    index = 1
    for i in range(n):
        a = float(data[index])
        b = float(data[index+1])
        index += 2
        participants.append((a, b, i+1))
    
    candidates = []
    for idx, (a, b, num) in enumerate(participants):
        max_total = a + b
        possible = True
        
        for j, (other_a, other_b, other_num) in enumerate(participants):
            if j == idx:
                continue
                
            total_other = other_a + other_b
            if total_other <= max_total:
                continue
                
            can_adjust = False
            for delta1 in [0, 100 - a]:
                for delta2 in [0, 100 - b]:
                    if delta1 == 0 and delta2 == 0:
                        continue
                    new_a = min(a + delta1, 100)
                    new_b = min(b + delta2, 100)
                    new_total = new_a + new_b
                    if new_total >= total_other:
                        can_adjust = True
                        break
                if can_adjust:
                    break
            
            if not can_adjust:
                possible = False
                break
                
        if possible:
            candidates.append(num)
            
    candidates.sort()
    print(len(candidates))
    if candidates:
        print(" ".join(map(str, candidates)))
    else:
        print()

if __name__ == "__main__":
    main()
