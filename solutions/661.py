
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    B = int(data[1])
    E = int(data[2])
    
    cards = []
    index = 3
    for i in range(n):
        bi = int(data[index])
        ei = int(data[index+1])
        si = int(data[index+2])
        index += 3
        if ei < B or bi > E:
            continue
        cards.append((bi, ei, si))
    
    if not cards:
        print(0)
        return
        
    cards.sort(key=lambda x: (x[0], -x[1]))
    
    max_e = -1
    filtered_cards = []
    for bi, ei, si in cards:
        if ei > max_e:
            filtered_cards.append((bi, ei, si))
            max_e = ei
    cards = filtered_cards
    
    n_cards = len(cards)
    dp = [float('inf')] * (n_cards + 1)
    dp[0] = 0
    
    for i in range(1, n_cards + 1):
        bi, ei, si = cards[i-1]
        if ei < B:
            continue
            
        if bi <= B:
            dp[i] = min(dp[i], si)
        else:
            left = 0
            right = i - 1
            while left <= right:
                mid = (left + right) // 2
                if cards[mid][1] >= bi:
                    right = mid - 1
                else:
                    left = mid + 1
            
            if left < i:
                dp[i] = min(dp[i], dp[left+1] + si)
        
        dp[i] = min(dp[i], dp[i-1])
    
    result = float('inf')
    for i in range(n_cards + 1):
        if cards[i-1][1] >= E if i > 0 else False:
            result = min(result, dp[i])
    
    print(result)

if __name__ == "__main__":
    main()
