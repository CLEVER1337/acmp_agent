
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    q = int(data[1])
    
    if q < n or q > 6 * n:
        print("0.0")
        return
        
    dp_prev = [0.0] * (6 * n + 1)
    dp_prev[0] = 1.0
    
    for i in range(1, n + 1):
        dp_curr = [0.0] * (6 * n + 1)
        for s in range(i - 1, 6 * (i - 1) + 1):
            if dp_prev[s] > 0:
                for d in range(1, 7):
                    if s + d <= 6 * n:
                        dp_curr[s + d] += dp_prev[s] / 6.0
        dp_prev = dp_curr
        
    print("{:.15f}".format(dp_prev[q]))

if __name__ == "__main__":
    main()
