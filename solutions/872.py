
def main():
    with open('INPUT.TXT', 'r') as f:
        m = int(f.readline().strip())
        words = [line.strip() for line in f.readlines()]
    
    words.sort(key=lambda x: len(x))
    
    dp = {}
    max_chain = 0
    
    for word in words:
        dp[word] = 1
        for i in range(1, len(word)):
            prefix = word[:i]
            if prefix in dp:
                dp[word] = max(dp[word], dp[prefix] + 1)
        max_chain = max(max_chain, dp[word])
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_chain))

if __name__ == '__main__':
    main()
