
def main():
    s = input().strip()
    patterns = {
        'aa': 3, 'aaa': 20, 'aaaa': 25,
        'ab': 0, 'aab': 10, 'aaab': 15,
        'abb': 5, 'abbb': 15, 'abba': 20,
        'abc': 0, 'aabb': 15, 'aabc': 10,
        'abcc': 10, 'abbc': 10, 'abcd': 0
    }
    
    n = len(s)
    dp = [-10**9] * (n + 1)
    dp[0] = 0
    path = [None] * (n + 1)
    
    for i in range(n + 1):
        for size in [2, 3, 4]:
            if i - size >= 0:
                group = s[i-size:i]
                pattern = get_pattern(group)
                score = patterns.get(pattern, 0)
                if dp[i] < dp[i-size] + score:
                    dp[i] = dp[i-size] + score
                    path[i] = (i-size, group)
    
    parts = []
    i = n
    while i > 0:
        prev, group = path[i]
        parts.append(group)
        i = prev
    
    parts.reverse()
    result = '-'.join(parts)
    print(result)
    print(dp[n])

def get_pattern(s):
    from collections import defaultdict
    mapping = {}
    pattern = []
    for char in s:
        if char not in mapping:
            mapping[char] = chr(ord('a') + len(mapping))
        pattern.append(mapping[char])
    return ''.join(pattern)

if __name__ == '__main__':
    main()
