
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    m = int(data[0])
    n = int(data[1])
    k = int(data[2])
    board = []
    index = 3
    for i in range(m):
        row = list(map(int, data[index:index+n]))
        index += n
        board.append(row)
    
    dp = [[-10**18] * (1 << m) for _ in range(k+1)]
    dp[0][0] = 0
    
    masks = []
    for mask in range(1 << m):
        if mask & (mask << 1):
            continue
        masks.append(mask)
    
    for col in range(n):
        new_dp = [[-10**18] * (1 << m) for _ in range(k+1)]
        for prev_mask in masks:
            for count in range(k+1):
                if dp[count][prev_mask] == -10**18:
                    continue
                for new_mask in masks:
                    if prev_mask & new_mask:
                        continue
                    cnt = bin(new_mask).count('1')
                    if count + cnt > k:
                        continue
                    total = dp[count][prev_mask]
                    for i in range(m):
                        if new_mask & (1 << i):
                            total += board[i][col] * board[i][col]
                    for i in range(m-1):
                        if (new_mask & (1 << i)) and (new_mask & (1 << (i+1))):
                            total += board[i][col] * board[i+1][col] * 2
                    new_dp[count + cnt][new_mask] = max(new_dp[count + cnt][new_mask], total)
        dp = new_dp
    
    result = max(dp[k])
    print(result)

if __name__ == "__main__":
    main()
