
def main():
    n = int(input().strip())
    if n == 1:
        print(8)
        return
        
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    
    dp_prev = [0] * 10
    for i in range(10):
        if i != 0 and i != 8:
            dp_prev[i] = 1
            
    for _ in range(2, n + 1):
        dp_curr = [0] * 10
        for digit in range(10):
            for prev_digit in moves[digit]:
                dp_curr[digit] += dp_prev[prev_digit]
        dp_prev = dp_curr
        
    print(sum(dp_prev))
    
if __name__ == "__main__":
    main()
