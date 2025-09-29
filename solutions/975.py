
import sys

def solve():
    data = sys.stdin.read().splitlines()
    results = []
    for line in data:
        if line.strip() == "0 0":
            break
        parts = line.split()
        if len(parts) < 2:
            continue
        N = int(parts[0])
        K = int(parts[1])
        
        if K == 1:
            results.append("1")
            continue
            
        min_lex = None
        
        def dfs(current):
            nonlocal min_lex
            if current > N:
                return
            if current % K == 0:
                if min_lex is None or str(current) < str(min_lex):
                    min_lex = current
                return
            for digit in range(10):
                next_num = current * 10 + digit
                if next_num > N:
                    continue
                dfs(next_num)
        
        for start in range(1, 10):
            dfs(start)
            
        if min_lex is not None:
            results.append(str(min_lex))
        else:
            results.append(str(K))
            
    sys.stdout.write("\n".join(results))

solve()
