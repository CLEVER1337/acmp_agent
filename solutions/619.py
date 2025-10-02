
def main():
    with open('INPUT.TXT', 'r') as f:
        N, Q = map(int, f.read().split())
    
    if Q < N or Q > 6 * N:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0.0')
        return
    
    dp_prev = [0] * (6 * N + 1)
    dp_prev[0] = 1
    
    for i in range(N):
        dp_curr = [0] * (6 * N + 1)
        for j in range(len(dp_prev)):
            if dp_prev[j] != 0:
                for k in range(1, 7):
                    if j + k < len(dp_curr):
                        dp_curr[j + k] += dp_prev[j]
        dp_prev = dp_curr
    
    favorable = dp_prev[Q]
    total = 6 ** N
    
    probability = favorable / total
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f'{probability:.15f}')

if __name__ == '__main__':
    main()
