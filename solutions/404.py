
import math

def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.readline().strip())
    
    if N == 0:
        with open("OUTPUT.TXT", "w") as f:
            f.write("LOSE")
        return
    
    dp = {}
    dp[0] = False
    
    k = int(math.isqrt(N))
    for i in range(1, k + 1):
        dp[i * i] = True
    
    for i in range(1, N + 1):
        if i not in dp:
            max_take = int(math.isqrt(i))
            can_win = False
            for take in range(1, max_take + 1):
                next_state = i - take
                if not dp.get(next_state, False):
                    can_win = True
                    break
            dp[i] = can_win
    
    result = "WIN" if dp[N] else "LOSE"
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
