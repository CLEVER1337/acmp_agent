
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, L = map(int, data[0].split())
    blocks = []
    for i in range(1, 1 + n):
        blocks.append(data[i].strip())
    s = data[1 + n].strip()
    
    len_s = len(s)
    INF = 10**9
    
    dp = [INF] * (len_s + 1)
    prev = [(-1, -1)] * (len_s + 1)
    dp[0] = 0
    
    for pos in range(len_s + 1):
        if dp[pos] == INF:
            continue
            
        for block_idx, block in enumerate(blocks):
            for start_col in range(L):
                match_len = 0
                for col in range(start_col, L):
                    if pos + match_len >= len_s:
                        break
                    if block[col] != s[pos + match_len]:
                        break
                    match_len += 1
                
                if match_len > 0:
                    new_pos = pos + match_len
                    if dp[new_pos] > dp[pos] + 1:
                        dp[new_pos] = dp[pos] + 1
                        prev[new_pos] = (pos, block_idx)
    
    if dp[len_s] == INF:
        print(-1)
    else:
        k = dp[len_s]
        result_blocks = []
        pos = len_s
        while pos > 0:
            prev_pos, block_idx = prev[pos]
            result_blocks.append(block_idx + 1)
            pos = prev_pos
            
        result_blocks.reverse()
        print(k)
        print(' '.join(map(str, result_blocks)))

if __name__ == "__main__":
    main()
