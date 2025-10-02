
def main():
    s = input().strip()
    patterns = {
        'aabb': 15, 'abba': 15, 'aaaa': 10, 'aaba': 8, 'abab': 8, 'aaab': 6, 'abaa': 6, 'abbb': 6, 'aabc': 4, 'abbc': 4, 'abcc': 4, 'abcd': 2
    }
    
    n = len(s)
    dp = [-10**9] * (n + 1)
    path = [None] * (n + 1)
    dp[0] = 0
    
    for i in range(n + 1):
        if dp[i] == -10**9:
            continue
        for size in [2, 3, 4]:
            if i + size <= n:
                group = s[i:i+size]
                pattern = get_pattern(group)
                score = patterns.get(pattern, 0)
                if dp[i + size] < dp[i] + score:
                    dp[i + size] = dp[i] + score
                    path[i + size] = (i, size)
    
    parts = []
    pos = n
    while pos > 0:
        prev, size = path[pos]
        parts.append(s[prev:pos])
        pos = prev
    parts.reverse()
    result = '-'.join(parts)
    print(result)
    print(dp[n])

def get_pattern(s):
    mapping = {}
    pattern = []
    for char in s:
        if char not in mapping:
            mapping[char] = chr(ord('a') + len(mapping))
        pattern.append(mapping[char])
    return ''.join(pattern)

if __name__ == "__main__":
    main()
