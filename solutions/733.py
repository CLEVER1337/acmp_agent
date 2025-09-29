
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    stack = []
    for num in a:
        while stack and stack[-1] <= num:
            if len(stack) >= 2 and stack[-2] > stack[-1]:
                stack.pop()
            else:
                break
        stack.append(num)
    
    while len(stack) >= 3:
        changed = False
        for i in range(1, len(stack)-1):
            if stack[i-1] > stack[i] and stack[i+1] > stack[i]:
                del stack[i]
                changed = True
                break
        if not changed:
            break
    
    print(len(stack))
    print(' '.join(map(str, stack)))

if __name__ == "__main__":
    main()
