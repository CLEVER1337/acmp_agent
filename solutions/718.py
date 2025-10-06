
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, l = map(int, data[0].split())
    blocks = []
    for i in range(1, 1 + n):
        blocks.append(data[i].strip())
    s = data[1 + n].strip()
    
    len_s = len(s)
    INF = 10**9
    dp = [INF] * (len_s + 1)
    prev_block = [-1] * (len_s + 1)
    prev_pos = [-1] * (len_s + 1)
    dp[0] = 0
    
    for pos in range(len_s + 1):
        if dp[pos] == INF:
            continue
        for idx, block in enumerate(blocks):
            block_len = len(block)
            if pos + block_len > len_s:
                continue
            match = True
            for i in range(block_len):
                if s[pos + i] != block[i]:
                    match = False
                    break
            if match:
                if dp[pos] + 1 < dp[pos + block_len]:
                    dp[pos + block_len] = dp[pos] + 1
                    prev_block[pos + block_len] = idx
                    prev_pos[pos + block_len] = pos
                    
    if dp[len_s] == INF:
        print(-1)
        return
        
    k = dp[len_s]
    result = []
    current = len_s
    while current > 0:
        result.append(prev_block[current] + 1)
        current = prev_pos[current]
        
    result.reverse()
    print(k)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
