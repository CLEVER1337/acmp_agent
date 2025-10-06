
def main():
    s = input().strip()
    patterns = {
        'a': 0, 'aa': 1, 'ab': 0, 'aaa': 2, 'aab': 1, 'aba': 1, 'abb': 1, 'abc': 0,
        'aaaa': 3, 'aaab': 1, 'aaba': 1, 'aabb': 2, 'abaa': 1, 'abab': 2, 'abba': 2, 
        'abbb': 1, 'abcc': 1, 'abcd': 0
    }
    
    n = len(s)
    dp = [-10**9] * (n + 1)
    parent = [None] * (n + 1)
    dp[0] = 0
    
    for i in range(n + 1):
        if dp[i] == -10**9:
            continue
        for l in [2, 3, 4]:
            if i + l <= n:
                part = s[i:i+l]
                pattern = []
                mapping = {}
                next_char = 'a'
                for char in part:
                    if char not in mapping:
                        mapping[char] = next_char
                        next_char = chr(ord(next_char) + 1)
                    pattern.append(mapping[char])
                pattern_str = ''.join(pattern)
                if pattern_str in patterns:
                    new_val = dp[i] + patterns[pattern_str]
                    if new_val > dp[i + l]:
                        dp[i + l] = new_val
                        parent[i + l] = (i, l)
    
    res = []
    cur = n
    while cur > 0:
        prev, l = parent[cur]
        res.append(s[prev:cur])
        cur = prev
    
    res.reverse()
    output = '-'.join(res)
    print(output)
    print(dp[n])

if __name__ == '__main__':
    main()
