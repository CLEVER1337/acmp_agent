
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        cities = []
        for _ in range(n):
            x, y = map(float, f.readline().split())
            cities.append((x, y))
    
    if n <= 1:
        print("0.00")
        return
    
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dx = cities[i][0] - cities[j][0]
            dy = cities[i][1] - cities[j][1]
            dist[i][j] = dist[j][i] = math.sqrt(dx*dx + dy*dy)
    
    min_r = float('inf')
    for i in range(n):
        max_dist = 0.0
        for j in range(n):
            if i != j and dist[i][j] > max_dist:
                max_dist = dist[i][j]
        if max_dist < min_r:
            min_r = max_dist
    
    print("{:.2f}".format(min_r/2))

if __name__ == "__main__":
    main()
