
import sys
import math
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    M = int(data[1])
    K = int(data[2])
    arr = list(map(int, data[3:3+n]))
    
    if n == 0:
        print(-1)
        return
        
    arr.sort()
    total_permutations = 0
    result = []
    used = [False] * n
    
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and math.gcd(arr[i], arr[j]) >= K:
                graph[i].append(j)
    
    memo = {}
    
    def count_permutations(mask, last):
        if mask == (1 << n) - 1:
            return 1
            
        if (mask, last) in memo:
            return memo[(mask, last)]
            
        total = 0
        for i in range(n):
            if not (mask & (1 << i)):
                if last == -1 or math.gcd(arr[last], arr[i]) >= K:
                    total += count_permutations(mask | (1 << i), i)
                    
        memo[(mask, last)] = total
        return total
        
    total_count = count_permutations(0, -1)
    if M > total_count:
        print(-1)
        return
        
    def find_mth(mask, last, m):
        if mask == (1 << n) - 1:
            return []
            
        candidates = []
        for i in range(n):
            if not (mask & (1 << i)):
                if last == -1 or math.gcd(arr[last], arr[i]) >= K:
                    cnt = count_permutations(mask | (1 << i), i)
                    candidates.append((i, cnt))
                    
        candidates.sort(key=lambda x: arr[x[0]])
        
        for i, cnt in candidates:
            if m <= cnt:
                next_mask = mask | (1 << i)
                rest = find_mth(next_mask, i, m)
                if rest is not None:
                    return [arr[i]] + rest
            else:
                m -= cnt
                
        return None
        
    result = find_mth(0, -1, M)
    if result:
        print(" ".join(map(str, result)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
