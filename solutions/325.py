
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().strip()
    
    start, end = data.split(', ')
    start_col, start_row = ord(start[0]) - ord('a'), int(start[1]) - 1
    end_col, end_row = ord(end[0]) - ord('a'), int(end[1]) - 1
    
    def is_knight_move(c1, r1, c2, r2):
        dc = abs(c1 - c2)
        dr = abs(r1 - r2)
        return (dc == 1 and dr == 2) or (dc == 2 and dr == 1)
    
    if is_knight_move(start_col, start_row, end_col, end_row):
        result = "1"
    else:
        found = False
        for dc1, dr1 in [(1,2), (2,1), (1,-2), (2,-1), (-1,2), (-2,1), (-1,-2), (-2,-1)]:
            mid_col = start_col + dc1
            mid_row = start_row + dr1
            if 0 <= mid_col < 8 and 0 <= mid_row < 8:
                if is_knight_move(mid_col, mid_row, end_col, end_row):
                    found = True
                    break
        
        result = "2" if found else "NO"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
