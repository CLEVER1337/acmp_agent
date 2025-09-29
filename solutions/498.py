
def main():
    with open("INPUT.TXT", "r") as f:
        n, k = map(int, f.read().split())
    
    from itertools import permutations
    
    count = 0
    for perm in permutations(range(1, n+1)):
        valid = True
        for i in range(len(perm)-1):
            if abs(perm[i] - perm[i+1]) > k:
                valid = False
                break
        if valid:
            count += 1
            
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
