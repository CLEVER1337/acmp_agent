
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    INF = float('inf')
    cost = [INF] * n
    cost[0] = 0
    
    dq = deque()
    dq.append(0)
    
    last_pos = {}
    
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
            
        if dq:
            cost[i] = cost[dq[0]] + (1 if s[dq[0]] != s[i] else 0)
        
        if s[i] in last_pos:
            j = last_pos[s[i]]
            if cost[j] <= cost[i]:
                cost[i] = cost[j]
        
        last_pos[s[i]] = i
        
        while dq and cost[i] <= cost[dq[-1]]:
            dq.pop()
        dq.append(i)
    
    print(cost[-1])

if __name__ == "__main__":
    main()
