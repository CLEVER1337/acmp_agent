
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.readline().split()
    
    start = data[0]
    end = data[1]
    
    def pos_to_coords(pos):
        col = ord(pos[0]) - ord('A')
        row = int(pos[1]) - 1
        return row, col
    
    def is_black(row, col):
        return (row + col) % 2 == 0
    
    start_row, start_col = pos_to_coords(start)
    end_row, end_col = pos_to_coords(end)
    
    if start_row == end_row and start_col == end_col:
        print(0)
        return
    
    n = 9
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    dist[start_row][start_col] = 0
    
    from collections import deque
    q = deque()
    q.append((start_row, start_col))
    
    bishop_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    
    while q:
        row, col = q.popleft()
        
        if row == end_row and col == end_col:
            break
            
        current_dist = dist[row][col]
        
        if is_black(row, col):
            moves = bishop_moves
        else:
            moves = knight_moves
            
        for dr, dc in moves:
            if is_black(row, col):
                r, c = row, col
                while True:
                    r += dr
                    c += dc
                    if 0 <= r < n and 0 <= c < n:
                        if dist[r][c] > current_dist + 1:
                            dist[r][c] = current_dist + 1
                            q.append((r, c))
                    else:
                        break
            else:
                r = row + dr
                c = col + dc
                if 0 <= r < n and 0 <= c < n:
                    if dist[r][c] > current_dist + 1:
                        dist[r][c] = current_dist + 1
                        q.append((r, c))
    
    result = dist[end_row][end_col]
    if result == INF:
        result = -1
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
