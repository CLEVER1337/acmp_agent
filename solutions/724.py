
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("Impossible")
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
    
    for k in range(1, m + 1):
        for attacks in combinations(range(1, m + 1), k):
            attacks_set = set(attacks)
            valid = True
            for row in matrix:
                found = False
                for j in range(m):
                    if row[j] == 1 and (j + 1) in attacks_set:
                        found = True
                        break
                if not found:
                    valid = False
                    break
            if valid:
                print(str(k) + " " + " ".join(map(str, attacks)))
                return
                
    print("Impossible")

if __name__ == "__main__":
    main()
