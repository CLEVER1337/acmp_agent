
def char_dist(c1, c2):
    base1 = ord('a') if c1.islower() else ord('A')
    base2 = ord('a') if c2.islower() else ord('A')
    idx1 = ord(c1) - base1
    idx2 = ord(c2) - base2
    diff = abs(idx1 - idx2)
    return min(diff, 26 - diff)

def word_dist(w1, w2):
    return sum(char_dist(a, b) for a, b in zip(w1, w2))

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    dictionary = data[1:1+n]
    text = data[1+n].strip()
    
    words = [w.lower() for w in dictionary]
    text_lower = text.lower()
    L = len(text)
    
    INF = float('inf')
    dp = [INF] * (L + 1)
    dp[0] = 0
    parent = [None] * (L + 1)
    
    for i in range(L + 1):
        if dp[i] == INF:
            continue
        for idx, word in enumerate(dictionary):
            w_lower = words[idx]
            w_len = len(w_lower)
            if i + w_len > L:
                continue
            segment = text_lower[i:i+w_len]
            dist_val = word_dist(word, text[i:i+w_len])
            if dp[i + w_len] > dp[i] + dist_val:
                dp[i + w_len] = dp[i] + dist_val
                parent[i + w_len] = (i, word)
    
    if dp[L] == INF:
        print(-1)
        return
        
    res = []
    pos = L
    while pos > 0:
        prev, word = parent[pos]
        res.append(word)
        pos = prev
    res.reverse()
    print(''.join(res))

if __name__ == "__main__":
    main()
