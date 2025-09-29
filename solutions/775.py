
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        M = int(data[1])
    
    if M == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('NO')
        return
    
    min_steps = collatz_steps(N)
    best_K = None
    best_steps = float('inf')
    
    for K in range(N + 1, N + M + 1):
        steps = collatz_steps(K)
        if steps < best_steps:
            best_steps = steps
            best_K = K
        elif steps == best_steps and K < best_K:
            best_K = K
    
    if best_steps < min_steps:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(str(best_K))
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('NO')

if __name__ == '__main__':
    main()
