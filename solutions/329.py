
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        stairs = list(map(int, f.readline().split()))
    
    dp = [0] * n
    path = [-1] * n
    
    dp[0] = stairs[0]
    if n > 1:
        dp[1] = max(stairs[0] + stairs[1], stairs[1])
        path[1] = 0 if stairs[0] + stairs[1] > stairs[1] else -1
    
    for i in range(2, n):
        option1 = dp[i-1] + stairs[i]
        option2 = dp[i-2] + stairs[i]
        
        if option1 >= option2:
            dp[i] = option1
            path[i] = i-1
        else:
            dp[i] = option2
            path[i] = i-2
    
    max_sum = dp[n-1]
    
    result_path = []
    current = n-1
    while current >= 0:
        result_path.append(current + 1)
        if path[current] == -1:
            break
        current = path[current]
    
    result_path.reverse()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_sum) + '\n')
        f.write(' '.join(map(str, result_path)) + '\n')

if __name__ == "__main__":
    main()
