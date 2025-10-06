
def main():
    s = input().strip()
    count = [0] * 26
    for char in s:
        idx = ord(char) - ord('A')
        count[idx] += 1
    
    required = [0] * 26
    for i in range(26):
        required[i] = i + 1
    
    current = [0] * 26
    for i in range(26):
        current[i] = count[i]
    
    for i in range(26):
        if sum(current[:i+1]) < required[i]:
            print("NO")
            return
    
    result = []
    used = [False] * 26
    for i in range(26):
        for j in range(26):
            if not used[j]:
                temp = current.copy()
                for k in range(26):
                    if k != j and not used[k]:
                        temp[k] -= 1
                
                valid = True
                for k in range(26):
                    if sum(temp[:k+1]) < required[k]:
                        valid = False
                        break
                
                if valid:
                    result.append(j + 1)
                    used[j] = True
                    current[j] -= 1
                    break
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
