
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    index = 0
    M = int(data[index]); index += 1
    shadows = []
    for i in range(M):
        W = int(data[index]); E = int(data[index+1]); index += 2
        shadows.append((W, E))
        
    N = int(data[index]); index += 1
    coords = []
    for i in range(N):
        coords.append(int(data[index])); index += 1
        
    coords.sort()
    
    dp = [0] * (N + 1)
    
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i])
        
        for W, E in shadows:
            left_bound = coords[i] - W
            right_bound = coords[i] + E
            
            j = i
            while j < N and coords[j] < right_bound:
                j += 1
                
            k = i
            while k >= 0 and coords[k] > left_bound:
                k -= 1
                
            next_pos = j
            dp[next_pos] = max(dp[next_pos], dp[k+1] + 1)
            
    print(dp[N])

if __name__ == "__main__":
    main()
