
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
    
    half = n // 2
    max_sum = 9 * half
    
    dp_prev = [0] * (max_sum + 1)
    dp_prev[0] = 1
    
    for _ in range(half):
        dp_curr = [0] * (max_sum + 1)
        for s in range(len(dp_prev)):
            if dp_prev[s] > 0:
                for d in range(10):
                    new_sum = s + d
                    if new_sum <= max_sum:
                        dp_curr[new_sum] += dp_prev[s]
        dp_prev = dp_curr
    
    count = sum(x * x for x in dp_prev)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
