
def main():
    with open('INPUT.TXT', 'r') as f:
        N, X, Y = map(int, f.read().split())
    
    size = 1 << N
    board = [[0] * size for _ in range(size)]
    board[Y-1][X-1] = -1
    
    counter = [1]
    
    def cover(x, y, size, hole_x, hole_y):
        if size == 1:
            return
        
        half = size // 2
        quadrant = 0
        if hole_x < x + half and hole_y < y + half:
            quadrant = 0
        elif hole_x >= x + half and hole_y < y + half:
            quadrant = 1
        elif hole_x < x + half and hole_y >= y + half:
            quadrant = 2
        else:
            quadrant = 3
        
        center_x = x + half - 1
        center_y = y + half - 1
        
        if quadrant != 0:
            board[center_y][center_x] = counter[0]
        if quadrant != 1:
            board[center_y][center_x + 1] = counter[0]
        if quadrant != 2:
            board[center_y + 1][center_x] = counter[0]
        if quadrant != 3:
            board[center_y + 1][center_x + 1] = counter[0]
        
        counter[0] += 1
        
        if quadrant == 0:
            cover(x, y, half, hole_x, hole_y)
        else:
            cover(x, y, half, center_x, center_y)
        
        if quadrant == 1:
            cover(x + half, y, half, hole_x, hole_y)
        else:
            cover(x + half, y, half, center_x + 1, center_y)
        
        if quadrant == 2:
            cover(x, y + half, half, hole_x, hole_y)
        else:
            cover(x, y + half, half, center_x, center_y + 1)
        
        if quadrant == 3:
            cover(x + half, y + half, half, hole_x, hole_y)
        else:
            cover(x + half, y + half, half, center_x + 1, center_y + 1)
    
    cover(0, 0, size, X-1, Y-1)
    
    with open('OUTPUT.TXT', 'w') as f:
        for row in board:
            f.write(' '.join(str(cell) if cell != -1 else '0' for cell in row) + '\n')

if __name__ == '__main__':
    main()
