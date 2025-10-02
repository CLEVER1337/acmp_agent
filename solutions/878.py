
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    count = [0] * 26
    
    for char in s:
        idx = ord(char) - ord('A')
        count[idx] += 1
    
    for i in range(26):
        if count[i] < i + 1:
            with open('OUTPUT.TXT', 'w') as f:
                f.write("NO\n")
            return
    
    result = []
    used = [False] * n
    for target in range(26):
        needed_char = chr(ord('A') + target)
        for i in range(n):
            if not used[i] and s[i] >= needed_char:
                result.append(i + 1)
                used[i] = True
                break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("YES\n")
        f.write(" ".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
