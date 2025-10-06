def point_in_rectangle(px, py, x1, y1, x2, y2, x3, y3, x4, y4):
    def triangle_area(ax, ay, bx, by, cx, cy):
        return abs((ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)))
    
    # Площадь прямоугольника
    area_rect = triangle_area(x1, y1, x2, y2, x3, y3) + triangle_area(x1, y1, x3, y3, x4, y4)
    
    # Сумма площадей треугольников, образованных точкой и сторонами прямоугольника
    area_sum = (triangle_area(px, py, x1, y1, x2, y2) +
                triangle_area(px, py, x2, y2, x3, y3) +
                triangle_area(px, py, x3, y3, x4, y4) +
                triangle_area(px, py, x4, y4, x1, y1))
    
    # Точка внутри, если сумма площадей треугольников равна площади прямоугольника
    # Учитываем возможные ошибки округления
    return abs(area_sum - area_rect) < 1e-9

def main():
    # Чтение входных данных
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    index = 1
    count = 0
    
    for _ in range(n):
        # Чтение координат дачника и его участка
        x = int(data[index]); y = int(data[index+1])
        x1 = int(data[index+2]); y1 = int(data[index+3])
        x2 = int(data[index+4]); y2 = int(data[index+5])
        x3 = int(data[index+6]); y3 = int(data[index+7])
        x4 = int(data[index+8]); y4 = int(data[index+9])
        index += 10
        
        # Проверяем, приземлился ли дачник на свой участок
        if point_in_rectangle(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
            count += 1
    
    # Запись результата
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
