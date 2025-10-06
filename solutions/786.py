
def main():
    n = int(input().strip())
    if n < 5:
        print(0)
        return
        
    dp = [False] * (n + 1)
    moves = []
    
    for i in range(5, n + 1):
        possible = False
        best_move = 0
        for j in range(1, (i + 1) // 2):
            if j != i - j:
                if not dp[i - j]:
                    possible = True
                    if best_move == 0 or j < best_move:
                        best_move = j
        dp[i] = possible
        if possible:
            moves.append(best_move)
        else:
            moves.append(0)
            
    if dp[n]:
        print(moves[n - 5])
    else:
        print(0)

if __name__ == "__main__":
    main()
