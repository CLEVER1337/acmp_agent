
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    K = int(data[0].strip())
    S = data[1].strip()
    n = len(S)
    
    last_occurrence = {}
    for idx, char in enumerate(S):
        last_occurrence[char] = idx
        
    freq = {}
    dq = deque()
    required_chars = set()
    
    for i in range(n):
        while dq and dq[0] < i - K + 1:
            dq.popleft()
            
        char = S[i]
        while dq and S[dq[-1]] >= char:
            dq.pop()
        dq.append(i)
        
        if i >= K - 1:
            min_char = S[dq[0]]
            required_chars.add(min_char)
            
    required_chars = sorted(required_chars)
    print(len(required_chars))
    for char in required_chars:
        print(char)

if __name__ == "__main__":
    main()
