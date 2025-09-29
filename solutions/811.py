
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    board = []
    for i in range(1, n+1):
        board.append(data[i].strip())
    
    # Две возможные правильные раскраски
    pattern1 = []
    pattern2 = []
    for i in range(n):
        row1 = []
        row2 = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row1.append('W')
                row2.append('B')
            else:
                row1.append('B')
                row2.append('W')
        pattern1.append(row1)
        pattern2.append(row2)
    
    # Считаем ошибки для обеих раскрасок
    errors1 = []
    errors2 = []
    count1 = 0
    count2 = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] != pattern1[i][j]:
                count1 += 1
                errors1.append((i+1, j+1))
            if board[i][j] != pattern2[i][j]:
                count2 += 1
                errors2.append((i+1, j+1))
    
    # Выбираем раскраску с меньшим количеством ошибок
    if count1 <= count2:
        print(count1)
        for error in errors1:
            print(f"{error[0]} {error[1]}")
    else:
        print(count2)
        for error in errors2:
            print(f"{error[0]} {error[1]}")

if __name__ == "__main__":
    main()
