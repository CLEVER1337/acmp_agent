
def main():
    with open('INPUT.TXT', 'r') as f:
        pos = f.read().strip()
    
    col = pos[0]
    row = int(pos[1])
    
    moves = []
    for dc, dr in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        new_col = chr(ord(col) + dc)
        new_row = row + dr
        
        if 'a' <= new_col <= 'h' and 1 <= new_row <= 8:
            moves.append(f"{new_col}{new_row}")
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(moves))

if __name__ == "__main__":
    main()
