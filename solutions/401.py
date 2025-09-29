
def main():
    with open("INPUT.TXT", "r") as f:
        N, A, B = map(int, f.read().split())
    
    from itertools import product
    
    count = 0
    for reds in product(range(A+1), repeat=N):
        if sum(reds) > A:
            continue
        for blues in product(range(B+1), repeat=N):
            if sum(blues) > B:
                continue
            valid = True
            for i in range(N):
                if reds[i] > 0 and blues[i] > 0:
                    valid = False
                    break
            if valid:
                count += 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
