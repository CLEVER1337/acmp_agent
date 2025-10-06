
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    orders = []
    index = 1
    max_day = 0
    for i in range(n):
        t = int(data[index])
        c = int(data[index+1])
        index += 2
        orders.append((t, c))
        if t > max_day:
            max_day = t
            
    orders.sort(key=lambda x: x[0])
    dp = [0] * (max_day + 1)
    
    for t, c in orders:
        for j in range(t, 0, -1):
            if dp[j] < dp[j-1] + c:
                dp[j] = dp[j-1] + c
                
    print(max(dp))

if __name__ == "__main__":
    main()
