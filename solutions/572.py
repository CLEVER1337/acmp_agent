
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    s = int(data[1])
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
    current_auth = s
    
    for a, b, idx in pos:
        if current_auth >= a:
            count += 1
            order.append(idx)
            current_auth += b
    
    dp = [[-10**18] * (count+1) for _ in range(len(neg)+1)]
    dp[0][0] = current_auth
    
    for i in range(1, len(neg)+1):
        a, b, idx = neg[i-1]
        for j in range(count+1):
            dp[i][j] = dp[i-1][j]
            if j > 0 and dp[i-1][j-1] >= a:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + b)
    
    max_friends = count
    for j in range(count, -1, -1):
        if dp[len(neg)][j] >= 0:
            max_friends += j
            break
    
    result_order = order[:]
    remaining = count
    selected = []
    
    for i in range(len(neg), 0, -1):
        a, b, idx = neg[i-1]
        if remaining > 0 and dp[i-1][remaining-1] >= a and dp[i-1][remaining-1] + b == dp[i][remaining]:
            selected.append(idx)
            remaining -= 1
    
    result_order.extend(selected[::-1])
    
    print(max_friends)
    print(' '.join(map(str, result_order)))

if __name__ == "__main__":
    main()
