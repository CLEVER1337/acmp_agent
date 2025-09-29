
def main():
    import sys
    from itertools import product
    
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    A = list(map(int, data[1].split()))
    B = []
    for i in range(2, 2+n):
        row = list(map(int, data[i].split()))
        B.append(row)
    
    possible_states = []
    for counts in product(*[range(A[i]+1) for i in range(n)]):
        valid = True
        for i in range(n):
            for j in range(i+1, n):
                if counts[i] > 0 and counts[j] > 0:
                    if B[i][j] and B[j][i]:
                        valid = False
                        break
                    elif B[i][j]:
                        if counts[j] < A[j]:
                            valid = False
                            break
                    elif B[j][i]:
                        if counts[i] < A[i]:
                            valid = False
                            break
            if not valid:
                break
        if valid:
            possible_states.append(counts)
    
    possible_states.sort()
    print(len(possible_states))
    for state in possible_states:
        print(' '.join(map(str, state)))

if __name__ == "__main__":
    main()
