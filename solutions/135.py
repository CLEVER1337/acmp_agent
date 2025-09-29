
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        graph = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            graph.append(row)
    
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    with open('OUTPUT.TXT', 'w') as f:
        for i in range(n):
            f.write(' '.join(map(str, dist[i])) + '\n')

if __name__ == '__main__':
    main()
