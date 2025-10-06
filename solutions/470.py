
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    H = int(data[idx]); W = int(data[idx+1]); N = int(data[idx+2]); idx += 3
    
    grid = []
    for i in range(H):
        row = list(map(int, data[idx:idx+W]))
        idx += W
        grid.append(row)
    
    prefix = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    output_lines = []
    for i in range(N):
        ai = int(data[idx]); bi = int(data[idx+1]); ci = int(data[idx+2]); di = int(data[idx+3]); idx += 4
        total = prefix[ci][di] - prefix[ai-1][di] - prefix[ci][bi-1] + prefix[ai-1][bi-1]
        output_lines.append(str(total))
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
