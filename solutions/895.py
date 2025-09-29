
def main():
    with open('INPUT.TXT', 'r') as f:
        board = [list(line.strip()) for line in f.readlines()]
    
    def check_win(player):
        # Проверка строк
        for row in board:
            if all(cell == player for cell in row):
                return True
        
        # Проверка столбцов
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        
        # Проверка диагоналей
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    x_win = check_win('X')
    o_win = check_win('O')
    
    if x_win and not o_win:
        result = 'Win'
    elif o_win and not x_win:
        result = 'Lose'
    else:
        result = 'Draw'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
