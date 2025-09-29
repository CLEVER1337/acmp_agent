
def main():
    with open('INPUT.TXT', 'r') as f:
        line1 = f.readline().split()
        line2 = f.readline().split()
    
    # Первый параллелепипед
    x11, y11, z11, x12, y12, z12 = map(int, line1)
    # Второй параллелепипед
    x21, y21, z21, x22, y22, z22 = map(int, line2)
    
    # Вычисляем объем первого параллелепипеда
    v1 = abs(x12 - x11) * abs(y12 - y11) * abs(z12 - z11)
    
    # Вычисляем объем второго параллелепипеда
    v2 = abs(x22 - x21) * abs(y22 - y21) * abs(z22 - z21)
    
    # Вычисляем объем пересечения
    # Находим пересечение по оси X
    x_overlap = max(0, min(x12, x22) - max(x11, x21))
    # Находим пересечение по оси Y
    y_overlap = max(0, min(y12, y22) - max(y11, y21))
    # Находим пересечение по оси Z
    z_overlap = max(0, min(z12, z22) - max(z11, z21))
    
    # Объем пересечения
    v_intersect = x_overlap * y_overlap * z_overlap
    
    # Общий объем = сумма объемов - объем пересечения
    total_volume = v1 + v2 - v_intersect
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total_volume))

if __name__ == "__main__":
    main()
