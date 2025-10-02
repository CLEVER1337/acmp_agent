
def circular_distance(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    if a_lower == b_lower:
        return 0
    pos_a = ord(a_lower) - ord('a')
    pos_b = ord(b_lower) - ord('a')
    diff = abs(pos_a - pos_b)
    return min(diff, 26 - diff)

def string_distance(s1, s2):
    return sum(circular_distance(s1[i], s2[i]) for i in range(len(s1)))

def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    dictionary = []
    for i in range(1, 1 + n):
        dictionary.append(data[i].strip())
    
    text = data[1 + n].strip()
    
    if not dictionary or not text:
        print(-1)
        return
        
    dp = [float('inf')] * (len(text) + 1)
    dp[0] = 0
    path = [None] * (len(text) + 1)
    
    for i in range(len(text) + 1):
        if dp[i] == float('inf'):
            continue
            
        for word in dictionary:
            j = i + len(word)
            if j > len(text):
                continue
                
            segment = text[i:j]
            dist = string_distance(segment, word)
            if dp[j] > dp[i] + dist:
                dp[j] = dp[i] + dist
                path[j] = (i, word)
    
    if dp[len(text)] == float('inf'):
        print(-1)
        return
        
    result = []
    pos = len(text)
    while pos > 0:
        prev, word = path[pos]
        result.append(word)
        pos = prev
        
    result.reverse()
    output = ''.join(result)
    print(output)

if __name__ == "__main__":
    main()
