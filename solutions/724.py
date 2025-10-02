
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        matrix.append(row)
    
    from itertools import combinations, product
    
    def covers(attacks, defense_row):
        for a in attacks:
            if defense_row[a] == 0:
                return True
        return False
    
    for k in range(1, m + 1):
        found_solution = True
        best_attacks = None
        
        for attack_set in combinations(range(m), k):
            valid = True
            for i in range(n):
                if not covers(attack_set, matrix[i]):
                    valid = False
                    break
            
            if valid:
                if best_attacks is None:
                    best_attacks = attack_set
                found_solution = True
                break
        
        if best_attacks is not None:
            result = [str(x + 1) for x in best_attacks]
            print(str(k))
            print(" ".join(result))
            return
    
    print("Impossible")

if __name__ == "__main__":
    main()
