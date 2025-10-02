
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    INF = float('inf')
    dp = [INF] * n
    dp[0] = 0
    
    last_occurrence = {}
    queue = deque()
    
    for i in range(n):
        char = s[i]
        if char in last_occurrence:
            dp[i] = min(dp[i], dp[last_occurrence[char]])
        
        while queue and queue[0] < i - k:
            queue.popleft()
            
        if queue:
            dp[i] = min(dp[i], dp[queue[0]] + 1)
            
        while queue and dp[queue[-1]] >= dp[i]:
            queue.pop()
        queue.append(i)
        
        last_occurrence[char] = i
    
    print(dp[n-1])

if __name__ == "__main__":
    main()
