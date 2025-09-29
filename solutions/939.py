
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        weights = list(map(int, f.readline().split()))
    
    total = sum(weights)
    if total % 3 != 0:
        with open("OUTPUT.TXT", "w") as f:
            f.write("0")
        return
    
    target = total // 3
    dp = [None] * (target + 1)
    dp[0] = []
    
    for i, w in enumerate(weights, 1):
        for s in range(target, w - 1, -1):
            if dp[s - w] is not None and dp[s] is None:
                dp[s] = dp[s - w] + [i]
    
    if dp[target] is None:
        with open("OUTPUT.TXT", "w") as f:
            f.write("0")
    else:
        with open("OUTPUT.TXT", "w") as f:
            f.write(f"{len(dp[target])}\n")
            f.write(" ".join(map(str, dp[target])))

if __name__ == "__main__":
    main()
