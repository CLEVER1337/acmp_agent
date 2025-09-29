
def main():
    s = input().strip()
    stack = []
    changes = 0
    
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        else:
            if not stack:
                changes += 1
                stack.append('(' if char == ')' else '[')
            else:
                top = stack.pop()
                if char == ')':
                    if top == '[':
                        changes += 1
                    elif top == '(':
                        pass
                    else:
                        stack.append(top)
                        changes += 1
                        stack.append('(')
                else:  # char == ']'
                    if top == '(':
                        changes += 1
                    elif top == '[':
                        pass
                    else:
                        stack.append(top)
                        changes += 1
                        stack.append('[')
    
    if stack:
        if len(stack) % 2 != 0:
            print(-1)
            return
        
        for i in range(0, len(stack), 2):
            if stack[i] == '(' and stack[i+1] == ')':
                pass
            elif stack[i] == '[' and stack[i+1] == ']':
                pass
            elif stack[i] == '(' and stack[i+1] == ']':
                changes += 1
            elif stack[i] == '[' and stack[i+1] == ')':
                changes += 1
            else:
                changes += 2
    
    print(changes)

if __name__ == "__main__":
    main()
