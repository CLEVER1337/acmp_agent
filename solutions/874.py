
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0]); k = int(data[1]); m = int(data[2])
    edges = []
    index = 3
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        edges.append((min(u, v)-1, max(u, v)-1))
    
    colors = [0] * n
    count = 0
    
    def is_valid(pos):
        for u, v in edges:
            if u < pos and v < pos:
                if colors[u] == colors[v]:
                    return False
        return True
    
    def backtrack(pos):
        nonlocal count
        if pos == n:
            count += 1
            return
        
        for color in range(k):
            colors[pos] = color
            if is_valid(pos):
                backtrack(pos + 1)
    
    backtrack(0)
    print(count)

if __name__ == "__main__":
    main()
