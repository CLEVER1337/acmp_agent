
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    
    stack = []
    count = 0
    
    for num in A:
        while stack and stack[-1] > num:
            stack.pop()
        if stack and stack[-1] == num:
            continue
        if num > 0:
            stack.append(num)
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
