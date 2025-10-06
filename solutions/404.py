
import math

def main():
    n = int(input().strip())
    if n == 0:
        print("LOSE")
        return
        
    dp = {}
    dp[0] = False
    
    def can_win(k):
        if k in dp:
            return dp[k]
            
        max_take = int(math.isqrt(k))
        if max_take == 0:
            dp[k] = False
            return False
            
        moves = set()
        for take in range(1, max_take + 1):
            moves.add(can_win(k - take))
            
        if False not in moves:
            dp[k] = False
        else:
            dp[k] = True
        return dp[k]
        
    if can_win(n):
        print("WIN")
    else:
        print("LOSE")

if __name__ == "__main__":
    main()
