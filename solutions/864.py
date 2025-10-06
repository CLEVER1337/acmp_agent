
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    
    total_moves = 0
    for i in range(n):
        if A[i] > 1:
            excess = A[i] - 1
            A[i] = 1
            j = (i + 1) % n
            while excess > 0:
                if A[j] < 1:
                    needed = 1 - A[j]
                    transfer = min(excess, needed)
                    A[j] += transfer
                    excess -= transfer
                    total_moves += transfer * min(abs(j - i), n - abs(j - i))
                j = (j + 1) % n
    
    print(total_moves)

if __name__ == "__main__":
    main()
