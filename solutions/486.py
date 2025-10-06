
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    X = 1
    while True:
        valid = True
        current = X
        for i in range(N):
            if (current - K) % N != 0 or current < K:
                valid = False
                break
            current = (current - K) * (N - 1) // N
        if valid:
            print(X)
            return
        X += 1

if __name__ == "__main__":
    main()
