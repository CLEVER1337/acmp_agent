
def main():
    with open('INPUT.TXT', 'r') as f:
        R, X, Y = map(int, f.read().split())
    
    # Координаты цели после отражения относительно стены
    X_reflected = X
    Y_reflected = 2 * R - Y
    
    # Расстояние от пушки до отраженной цели
    distance = (X_reflected**2 + Y_reflected**2)**0.5
    
    # Точка удара о стену находится на пересечении прямой к отраженной цели и стены
    # Используем подобие треугольников
    wall_x = (R * X_reflected) / Y_reflected
    
    print("{:.2f}".format(wall_x))

if __name__ == "__main__":
    main()
