
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
    target = data[1 + n].strip()
    len_target = len(target)
    
    # DP: dp[i] = (min_blocks, prev_block_index, prev_state)
    # state: which column we're at in the current block
    
    INF = float('inf')
    dp = [INF] * (len_target + 1)
    prev = [(-1, -1)] * (len_target + 1)
    dp[0] = 0
    
    for i in range(len_target + 1):
        if dp[i] == INF:
            continue
            
        # Try to add a new block on top
        for block_idx, block in enumerate(blocks):
            # Check how many characters we can match from this block
            for start_col in range(L):
                match_len = 0
                # Check matching from position i in target and column start_col in block
                for col in range(start_col, L):
                    pos = i + (col - start_col)
                    if pos >= len_target:
                        break
                    if target[pos] != block[col]:
                        break
                    match_len += 1
                
                if match_len > 0:
                    new_pos = i + match_len
                    if dp[new_pos] > dp[i] + 1:
                        dp[new_pos] = dp[i] + 1
                        prev[new_pos] = (i, block_idx)
    
    if dp[len_target] == INF:
        print(-1)
        return
        
    # Reconstruct the solution
    k = dp[len_target]
    result_blocks = []
    pos = len_target
    while pos > 0:
        prev_pos, block_idx = prev[pos]
        result_blocks.append(block_idx + 1)
        pos = prev_pos
        
    result_blocks.reverse()
    print(k)
    print(' '.join(map(str, result_blocks)))

if __name__ == "__main__":
    main()
