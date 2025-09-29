
import math

def min_operations(n, m):
    if n == m:
        return 0
    if n > m:
        return -1
    
    queue = [(n, 0)]
    visited = set()
    visited.add(n)
    
    while queue:
        current, steps = queue.pop(0)
        
        if current == m:
            return steps
        
        next1 = current * 2
        if next1 <= m and next1 not in visited:
            visited.add(next1)
            queue.append((next1, steps + 1))
        
        next2 = current * 3
        if next2 <= m and next2 not in visited:
            visited.add(next2)
            queue.append((next2, steps + 1))
    
    return -1

def main():
    with open("INPUT.TXT", "r") as f:
        n, m = map(int, f.readline().split())
    
    if n == m:
        print(0)
        return
    
    if m % n != 0:
        print(-1)
        return
    
    quotient = m // n
    operations = 0
    
    while quotient > 1:
        if quotient % 2 == 0:
            quotient //= 2
            operations += 1
        elif quotient % 3 == 0:
            quotient //= 3
            operations += 1
        else:
            print(-1)
            return
    
    print(operations)

if __name__ == "__main__":
    main()
