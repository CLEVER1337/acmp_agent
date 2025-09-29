
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        total_pairs = n * (n + 1) // 2
        costs = []
        
        while len(costs) < total_pairs:
            line = f.readline().strip()
            if line:
                costs.extend(map(int, line.split()))
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        idx = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] + costs[idx] < dp[j]:
                    dp[j] = dp[i] + costs[idx]
                idx += 1
        
        with open('OUTPUT.TXT', 'w') as f_out:
            f_out.write(str(dp[n]))

if __name__ == "__main__":
    main()
