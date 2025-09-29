
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    h = int(data[0])
    w = int(data[1])
    n = int(data[2])
    
    matrix = []
    index = 3
    for i in range(h):
        row = list(map(int, data[index:index+w]))
        index += w
        matrix.append(row)
    
    prefix = [[0] * (w + 1) for _ in range(h + 1)]
    
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    results = []
    for _ in range(n):
        ai = int(data[index])
        bi = int(data[index+1])
        ci = int(data[index+2])
        di = int(data[index+3])
        index += 4
        
        total = prefix[ci][di] - prefix[ai-1][di] - prefix[ci][bi-1] + prefix[ai-1][bi-1]
        results.append(str(total))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
