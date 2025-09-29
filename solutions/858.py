
def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    coeffs = []
    for line in lines:
        a, b, c = map(int, line.strip().split())
        coeffs.append((a, b, c))
    
    # Находим точки пересечения прямых
    intersections = []
    for i in range(3):
        j = (i + 1) % 3
        a1, b1, c1 = coeffs[i]
        a2, b2, c2 = coeffs[j]
        
        # Решаем систему уравнений:
        # a1*x + b1*y = c1
        # a2*x + b2*y = c2
        
        det = a1 * b2 - a2 * b1
        if det == 0:
            # Прямые параллельны или совпадают
            print("0.000")
            return
        
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        intersections.append((x, y))
    
    # Вычисляем площадь треугольника по координатам вершин
    x1, y1 = intersections[0]
    x2, y2 = intersections[1]
    x3, y3 = intersections[2]
    
    area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.3f}".format(area))

if __name__ == "__main__":
    main()
