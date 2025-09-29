
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    containers = []
    for i in range(1, n+1):
        row = list(map(int, data[i].split()))
        containers.append(row)
    
    total_bottles = [0] * n
    for i in range(n):
        for j in range(n):
            total_bottles[j] += containers[i][j]
    
    from itertools import permutations
    best_cost = float('inf')
    best_perm = None
    
    for perm in permutations(range(n)):
        cost = 0
        for i in range(n):
            for j in range(n):
                if j != perm[i]:
                    cost += containers[i][j]
        if cost < best_cost:
            best_cost = cost
            best_perm = perm
    
    letters = [chr(ord('A') + i) for i in range(n)]
    result_letters = [letters[i] for i in best_perm]
    
    print(' '.join(result_letters))
    print(best_cost)

if __name__ == "__main__":
    main()
