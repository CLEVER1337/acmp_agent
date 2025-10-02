
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        sides = list(map(float, f.readline().split()))
    
    a, b, c = sorted(sides)
    
    # Проверяем, является ли треугольник прямоугольным
    if math.isclose(a**2 + b**2, c**2, rel_tol=1e-9):
        area = 0.5 * a * b
        with open('OUTPUT.TXT', 'w') as f:
            f.write(f"{area:.10f}")
        return
    
    # Если треугольник остроугольный
    if a**2 + b**2 > c**2:
        # Максимальная площадь - когда гипотенуза совпадает с наибольшей стороной
        # Катеты будут максимально возможными при этом условии
        h = 2 * (a * b * c) / (a**2 + b**2 + c**2)
        cat1 = math.sqrt(a**2 - h**2)
        cat2 = math.sqrt(b**2 - h**2)
        area = 0.5 * cat1 * cat2
        with open('OUTPUT.TXT', 'w') as f:
            f.write(f"{area:.10f}")
        return
    
    # Если треугольник тупоугольный
    # Максимальная площадь достигается, когда прямой угол находится
    # в вершине напротив наибольшей стороны
    # Используем формулу для площади через высоту
    p = (a + b + c) / 2
    area_triangle = math.sqrt(p * (p - a) * (p - b) * (p - c))
    h = 2 * area_triangle / c
    
    # Катеты прямоугольного треугольника
    cat1 = math.sqrt(a**2 - h**2)
    cat2 = math.sqrt(b**2 - h**2)
    area = 0.5 * cat1 * cat2
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{area:.10f}")

if __name__ == "__main__":
    main()
