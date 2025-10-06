
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    
    stack = []
    count = 0
    
    for h in A:
        while stack and stack[-1] > h:
            stack.pop()
        if stack and stack[-1] == h:
            continue
        if h > 0:
            stack.append(h)
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
