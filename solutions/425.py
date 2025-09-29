
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    W = int(data[1])
    E = int(data[2])
    
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            x_left = 100 * i - 100
            x_right = 100 * i
            y_bottom = 100 * j - 100
            y_top = 100 * j
            
            # Уравнение прямой: y = k*x + b
            # Прямая проходит через (0, W) и (100*N, E)
            if 100 * N != 0:
                k = (E - W) / (100 * N)
            else:
                k = 0
            b = W
            
            # Проверяем пересечение прямой с квадратом
            # Проверяем пересечение с вертикальными гранями
            if k != 0:
                y1 = k * x_left + b
                y2 = k * x_right + b
                if min(y1, y2) <= y_top and max(y1, y2) >= y_bottom:
                    count += 1
                    continue
            
            # Проверяем пересечение с горизонтальными гранями
            if k != 0:
                x1 = (y_bottom - b) / k
                x2 = (y_top - b) / k
                if min(x1, x2) <= x_right and max(x1, x2) >= x_left:
                    count += 1
                    continue
            
            # Случай горизонтальной прямой
            if k == 0:
                if y_bottom <= W <= y_top:
                    count += 1
                    continue
    
    print(count)

if __name__ == "__main__":
    main()
