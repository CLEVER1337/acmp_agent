
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        permutation = list(map(int, f.readline().split()))
    
    visited = [False] * (n + 1)
    cycles_lengths = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            cycle_length = 0
            current = i
            
            while not visited[current]:
                visited[current] = True
                current = permutation[current - 1]
                cycle_length += 1
            
            if cycle_length > 0:
                cycles_lengths.append(cycle_length)
    
    result = 1
    for length in cycles_lengths:
        result = lcm(result, length)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
