
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    K = int(data[0].strip())
    s = data[1].strip()
    n = len(s)
    
    freq = [0] * 26
    last_occurrence = [-1] * 26
    required = set()
    
    dq = deque()
    
    for i in range(n):
        c = s[i]
        idx = ord(c) - ord('A')
        last_occurrence[idx] = i
        
        while dq and dq[-1][0] > idx:
            dq.pop()
        dq.append((idx, i))
        
        if i >= K - 1:
            while dq and dq[0][1] <= i - K:
                dq.popleft()
            if dq:
                min_char_idx = dq[0][0]
                required.add(min_char_idx)
    
    result_chars = sorted(chr(ord('A') + idx) for idx in required)
    
    print(len(result_chars))
    for char in result_chars:
        print(char)

if __name__ == "__main__":
    main()
