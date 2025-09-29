
import collections

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    dp = [float('inf')] * n
    dp[0] = 0
    
    dq = collections.deque()
    dq.append(0)
    
    last_occurrence = {}
    
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
            
        if dq:
            prev_index = dq[0]
            cost = dp[prev_index] + (1 if s[i] != s[prev_index] else 0)
            dp[i] = min(dp[i], cost)
        
        if s[i] in last_occurrence:
            prev_same_char_index = last_occurrence[s[i]]
            if dp[prev_same_char_index] <= dp[i]:
                dp[i] = dp[prev_same_char_index]
        
        last_occurrence[s[i]] = i
        
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
    
    print(dp[n-1])

if __name__ == "__main__":
    main()
