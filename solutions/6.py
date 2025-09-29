
def check_move(move):
    if len(move) != 5 or move[2] != '-':
        return 'ERROR'
    
    start, end = move.split('-')
    
    if not (start[0].isalpha() and start[1].isdigit() and end[0].isalpha() and end[1].isdigit()):
        return 'ERROR'
        
    start_x, start_y = ord(start[0]) - 65, int(start[1]) - 1
    end_x, end_y = ord(end[0]) - 65, int(end[1]) - 1
    
    if not (0 <= start_x < 8 and 0 <= start_y < 8 and 0 <= end_x < 8 and 0 <= end_y < 8):
        return 'ERROR'
        
    dx = abs(start_x - end_x)
    dy = abs(start_y - end_y)
    
    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
        return 'YES'
    else:
        return 'NO'

with open('INPUT.TXT', 'r') as f:
    move = f.readline().strip()
    
result = check_move(move)

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
