
def main():
    with open('INPUT.TXT', 'r') as f:
        n, s = map(int, f.readline().split())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
    
    visited = [False] * n
    stack = [s - 1]
    visited[s - 1] = True
    count = 0
    
    while stack:
        current = stack.pop()
        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
