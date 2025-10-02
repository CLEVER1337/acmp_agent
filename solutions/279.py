
def main():
    with open("INPUT.TXT", "r") as f:
        s = f.readline().strip()
    
    n = len(s)
    if n % 2 != 0:
        print(-1)
        return
        
    stack = []
    changes = 0
    
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        else:
            if not stack:
                print(-1)
                return
                
            top = stack.pop()
            if char == ')':
                if top != '(' and top != '[':
                    print(-1)
                    return
                if top == '[':
                    changes += 1
            else:  # char == ']'
                if top != '[' and top != '(':
                    print(-1)
                    return
                if top == '(':
                    changes += 1
                    
    if stack:
        print(-1)
    else:
        print(changes)

if __name__ == "__main__":
    main()
