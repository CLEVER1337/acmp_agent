
def main():
    s = input().strip()
    n = len(s)
    if n % 2 != 0:
        print("NO")
        return
        
    pairs = {'(': ')', '[': ']', '{': '}', ')': '(', ']': '[', '}': '{'}
    
    def check(t):
        stack = []
        for char in t:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[top] != char:
                    return False
        return len(stack) == 0
        
    for i in range(n):
        shifted = s[i:] + s[:i]
        if check(shifted):
            print("YES")
            return
            
    print("NO")

if __name__ == "__main__":
    main()
