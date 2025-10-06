
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        N = int(data[0])
        A = int(data[1])
        B = int(data[2])
    
    dp = [[[[0 for _ in range(B+1)] for _ in range(A+1)] for _ in range(B+1)] for _ in range(A+1)]
    dp[0][0][0][0] = 1
    
    for box in range(N):
        new_dp = [[[[0 for _ in range(B+1)] for _ in range(A+1)] for _ in range(B+1)] for _ in range(A+1)]
        for a_used in range(A+1):
            for b_used in range(B+1):
                for a_left in range(A+1 - a_used):
                    for b_left in range(B+1 - b_used):
                        if dp[a_used][b_used][a_left][b_left] == 0:
                            continue
                        current = dp[a_used][b_used][a_left][b_left]
                        
                        for red in range(0, min(a_left, A - a_used) + 1):
                            for blue in range(0, min(b_left, B - b_used) + 1):
                                new_a_used = a_used + red
                                new_b_used = b_used + blue
                                new_a_left = a_left - red
                                new_b_left = b_left - blue
                                new_dp[new_a_used][new_b_used][new_a_left][new_b_left] += current
        
        dp = new_dp
    
    total = 0
    for a_used in range(A+1):
        for b_used in range(B+1):
            for a_left in range(A+1 - a_used):
                for b_left in range(B+1 - b_used):
                    total += dp[a_used][b_used][a_left][b_left]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(total))

if __name__ == "__main__":
    main()
