
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
    
    n_steps = collatz_steps(N)
    best_k = None
    best_steps = float('inf')
    
    for k in range(N + 1, N + M + 1):
        steps = collatz_steps(k)
        if steps < n_steps:
            if steps < best_steps or (steps == best_steps and k < best_k):
                best_k = k
                best_steps = steps
    
    if best_k is not None:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(str(best_k))
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('NO')

if __name__ == '__main__':
    main()
