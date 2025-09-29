
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.readline().split()
    
    wk, wq, bk = data
    
    def pos_to_coords(pos):
        col = ord(pos[0]) - ord('A')
        row = int(pos[1]) - 1
        return col, row
    
    wq_col, wq_row = pos_to_coords(wq)
    bk_col, bk_row = pos_to_coords(bk)
    wk_col, wk_row = pos_to_coords(wk)
    
    # Проверяем, находится ли черный король на линии атаки ферзя
    if wq_col == bk_col or wq_row == bk_row or abs(wq_col - bk_col) == abs(wq_row - bk_row):
        # Проверяем, не блокирует ли белый король линию атаки
        if wq_col == bk_col == wk_col:
            if (wq_row < wk_row < bk_row) or (bk_row < wk_row < wq_row):
                result = "NO"
            else:
                result = "YES"
        elif wq_row == bk_row == wk_row:
            if (wq_col < wk_col < bk_col) or (bk_col < wk_col < wq_col):
                result = "NO"
            else:
                result = "YES"
        elif abs(wq_col - bk_col) == abs(wq_row - bk_row):
            if abs(wq_col - wk_col) == abs(wq_row - wk_row):
                # Проверяем, находится ли король между ферзем и черным королем
                if (wq_col < wk_col < bk_col or bk_col < wk_col < wq_col) and \
                   (wq_row < wk_row < bk_row or bk_row < wk_row < wq_row):
                    result = "NO"
                else:
                    result = "YES"
            else:
                result = "YES"
        else:
            result = "YES"
    else:
        result = "NO"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
