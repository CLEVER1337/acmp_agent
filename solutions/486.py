
def main():
    with open('INPUT.TXT', 'r') as f:
        N, K = map(int, f.readline().split())
    
    X = 1
    while True:
        valid = True
        current = X
        for i in range(N):
            if (current - K) % N != 0:
                valid = False
                break
            current = (current - K) // N * (N - 1)
        
        if valid:
            break
        X += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(X))

if __name__ == '__main__':
    main()
