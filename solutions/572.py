
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    auth = int(data[1])
    friends = []
    index = 2
    for i in range(n):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        friends.append((a, b, i+1))
        
    pos = []
    neg = []
    for a, b, idx in friends:
        if b >= 0:
            pos.append((a, b, idx))
        else:
            neg.append((a, b, idx))
            
    pos.sort(key=lambda x: x[0])
    neg.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    count = 0
    order = []
    current_auth = auth
    
    for a, b, idx in pos:
        if current_auth >= a:
            count += 1
            order.append(idx)
            current_auth += b
            
    dp = [[-10**18] * (len(neg)+1) for _ in range(len(neg)+1)]
    dp[0][0] = current_auth
    best_count = 0
    best_state = 0
    
    for i in range(len(neg)):
        a, b, idx = neg[i]
        for j in range(i+1):
            if dp[i][j] == -10**18:
                continue
            if dp[i][j] >= a:
                if dp[i+1][j+1] < dp[i][j] + b:
                    dp[i+1][j+1] = dp[i][j] + b
            if dp[i+1][j] < dp[i][j]:
                dp[i+1][j] = dp[i][j]
                
    for j in range(len(neg)+1):
        if dp[len(neg)][j] != -10**18:
            best_count = j
            best_state = j
            
    selected = []
    j = best_count
    for i in range(len(neg)-1, -1, -1):
        if j > 0 and dp[i][j-1] != -10**18 and dp[i][j-1] >= neg[i][0] and dp[i][j-1] + neg[i][1] == dp[i+1][j]:
            selected.append(neg[i][2])
            j -= 1
            
    total_count = count + best_count
    result_order = order + selected
    
    print(total_count)
    if total_count > 0:
        print(" ".join(map(str, result_order)))
    else:
        print()

if __name__ == "__main__":
    main()
