
def main():
    import sys
    sys.setrecursionlimit(10000)
    
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        matrix.append(row)
    
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue
            
        for i in range(n):
            if not (mask & (1 << i)):
                can_add = True
                for j in range(n):
                    if mask & (1 << j):
                        if matrix[i][j] == 1:
                            can_add = False
                            break
                if can_add:
                    new_mask = mask | (1 << i)
                    dp[new_mask] = min(dp[new_mask], dp[mask])
                    
                for j in range(i + 1, n):
                    if not (mask & (1 << j)) and not (mask & (1 << i)):
                        compatible = True
                        if matrix[i][j] == 1:
                            compatible = False
                        else:
                            for k in range(n):
                                if mask & (1 << k):
                                    if matrix[i][k] == 1 or matrix[j][k] == 1:
                                        compatible = False
                                        break
                        if compatible:
                            new_mask = mask | (1 << i) | (1 << j)
                            dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
                
                break
    
    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue
        for i in range(n):
            if not (mask & (1 << i)):
                for j in range(i + 1, n):
                    if not (mask & (1 << j)):
                        compatible = True
                        for k in range(n):
                            if mask & (1 << k):
                                if matrix[i][k] == 1 or matrix[j][k] == 1:
                                    compatible = False
                                    break
                        if compatible and matrix[i][j] == 0:
                            new_mask = mask | (1 << i) | (1 << j)
                            dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
    
    print(dp[(1 << n) - 1])

if __name__ == "__main__":
    main()
