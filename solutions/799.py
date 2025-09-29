
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = list(map(int, data[1:1+n]))
    
    dad_candidates = []
    for i in range(n):
        if scores[i] % 10 == 5:
            dad_candidates.append(i)
            
    if not dad_candidates:
        print(0)
        return
        
    best_place = float('inf')
    
    for dad_index in dad_candidates:
        dad_score = scores[dad_index]
        
        if dad_index == n - 1:
            continue
            
        friend_score = scores[dad_index + 1]
        if friend_score >= dad_score:
            continue
            
        has_better_before = False
        for i in range(dad_index):
            if scores[i] > dad_score:
                has_better_before = True
                break
                
        if not has_better_before:
            continue
            
        better_count = 0
        for i in range(n):
            if scores[i] > dad_score:
                better_count += 1
                
        place = better_count + 1
        
        if place < best_place:
            best_place = place
            
    if best_place == float('inf'):
        print(0)
    else:
        print(best_place)

if __name__ == "__main__":
    main()
