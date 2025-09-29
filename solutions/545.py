
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        sides = list(map(float, f.readline().split()))
    
    a, b, c = sorted(sides)
    
    # Проверяем, является ли треугольник прямоугольным
    if abs(a**2 + b**2 - c**2) < 1e-9:
        area = 0.5 * a * b
        with open('OUTPUT.TXT', 'w') as f:
            f.write(f"{area:.10f}")
        return
    
    # Рассматриваем три варианта прямоугольных треугольников:
    # 1. Катеты на сторонах a и b
    # 2. Катеты на сторонах a и c  
    # 3. Катеты на сторонах b и c
    
    max_area = 0.0
    
    # Вариант 1: катеты на сторонах a и b
    if a > 0 and b > 0:
        area1 = 0.5 * a * b
        max_area = max(max_area, area1)
    
    # Вариант 2: катеты на сторонах a и c
    if a > 0 and c > 0:
        # Находим высоту от вершины между сторонами a и c к стороне b
        p = (a + b + c) / 2
        area_total = math.sqrt(p * (p - a) * (p - b) * (p - c))
        h = 2 * area_total / b
        
        if h <= a:
            angle = math.asin(h / a)
            cathet1 = a * math.cos(angle)
            cathet2 = h
            area2 = 0.5 * cathet1 * cathet2
            max_area = max(max_area, area2)
        else:
            area2 = 0.5 * a * min(a, c)
            max_area = max(max_area, area2)
    
    # Вариант 3: катеты на сторонах b и c
    if b > 0 and c > 0:
        # Находим высоту от вершины между сторонами b и c к стороне a
        p = (a + b + c) / 2
        area_total = math.sqrt(p * (p - a) * (p - b) * (p - c))
        h = 2 * area_total / a
        
        if h <= b:
            angle = math.asin(h / b)
            cathet1 = b * math.cos(angle)
            cathet2 = h
            area3 = 0.5 * cathet1 * cathet2
            max_area = max(max_area, area3)
        else:
            area3 = 0.5 * b * min(b, c)
            max_area = max(max_area, area3)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{max_area:.10f}")

if __name__ == "__main__":
    main()
