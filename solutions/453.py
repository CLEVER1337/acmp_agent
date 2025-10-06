
from collections import deque

def main():
    n = int(input().strip())
    target = 2 * n
    
    if n == 1:
        print(2)
        return
    
    visited = [False] * target
    parent = [-1] * target
    digit = [-1] * target
    
    queue = deque()
    queue.append(1 % target)
    visited[1 % target] = True
    digit[1 % target] = 1
    
    queue.append(2 % target)
    visited[2 % target] = True
    digit[2 % target] = 2
    
    found = -1
    while queue:
        current = queue.popleft()
        if current == 0:
            found = current
            break
            
        for next_digit in [1, 2]:
            next_remainder = (current * 10 + next_digit) % target
            if not visited[next_remainder]:
                visited[next_remainder] = True
                parent[next_remainder] = current
                digit[next_remainder] = next_digit
                queue.append(next_remainder)
                if next_remainder == 0:
                    found = next_remainder
                    break
        if found != -1:
            break
            
    result = []
    current = found
    while current != -1:
        result.append(str(digit[current]))
        current = parent[current]
    
    result.reverse()
    print(''.join(result))

if __name__ == "__main__":
    main()
