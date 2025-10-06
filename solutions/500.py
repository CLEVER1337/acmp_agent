
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    agents = []
    index = 1
    for i in range(n):
        age = int(data[index])
        risk = int(data[index+1])
        index += 2
        agents.append((age, risk))
    
    agents.sort()
    
    if n == 2:
        print(min(agents[0][1], agents[1][1]))
        return
        
    dp = [0] * n
    dp[0] = agents[0][1]
    dp[1] = agents[1][1]
    
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + agents[i][1]
    
    print(min(dp[n-1], dp[n-2]))

if __name__ == "__main__":
    main()
