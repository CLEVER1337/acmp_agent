
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    orders = []
    index = 1
    max_deadline = 0
    for i in range(n):
        t = int(data[index])
        c = int(data[index + 1])
        index += 2
        orders.append((t, c))
        if t > max_deadline:
            max_deadline = t
            
    orders.sort(key=lambda x: x[0])
    
    dp = [0] * (max_deadline + 1)
    
    for deadline, cost in orders:
        for j in range(deadline, 0, -1):
            if dp[j] < dp[j - 1] + cost:
                dp[j] = dp[j - 1] + cost
                
    print(max(dp))

if __name__ == "__main__":
    main()
