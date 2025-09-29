
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    dictionary = []
    for i in range(1, 1 + n):
        dictionary.append(data[i].strip())
    text = data[1 + n].strip()
    
    def char_distance(c1, c2):
        if c1 == c2:
            return 0
        c1_lower = c1.lower()
        c2_lower = c2.lower()
        if c1_lower == c2_lower:
            return 0
        pos1 = ord(c1_lower) - ord('a')
        pos2 = ord(c2_lower) - ord('a')
        diff = abs(pos1 - pos2)
        return min(diff, 26 - diff)
    
    INF = float('inf')
    dp = [INF] * (len(text) + 1)
    dp[0] = 0
    parent = [(-1, -1)] * (len(text) + 1)
    
    for i in range(len(text) + 1):
        if dp[i] == INF:
            continue
        for word in dictionary:
            j = i + len(word)
            if j > len(text):
                continue
            cost = 0
            for k in range(len(word)):
                cost += char_distance(text[i + k], word[k])
            if dp[j] > dp[i] + cost:
                dp[j] = dp[i] + cost
                parent[j] = (i, word)
    
    if dp[len(text)] == INF:
        print(-1)
        return
    
    result = []
    pos = len(text)
    while pos > 0:
        prev, word = parent[pos]
        result.append(word)
        pos = prev
    result.reverse()
    print(''.join(result))

if __name__ == '__main__':
    main()
