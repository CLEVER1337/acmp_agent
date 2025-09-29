
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        d, r = map(float, f.readline().split())
        n = int(f.readline().strip())
    
    # Общая площадь сосиски
    area_total = math.pi * r * r + 2 * r * d
    
    # Площадь одного куска
    area_per_piece = area_total / n
    
    # Функция для вычисления площади от левого края до точки x
    def area_to_x(x):
        if x <= r:
            # В пределах левого полукруга
            theta = math.acos((r - x) / r)
            segment_area = r * r * theta - (r - x) * math.sqrt(r * r - (r - x) * (r - x))
            return segment_area
        elif x <= d:
            # В центральной прямоугольной части
            circle_area = math.pi * r * r / 2
            rect_area = 2 * r * (x - r)
            return circle_area + rect_area
        else:
            # В правом полукруге
            x_from_right = d + 2 * r - x
            theta = math.acos((r - x_from_right) / r)
            segment_area = r * r * theta - (r - x_from_right) * math.sqrt(r * r - (r - x_from_right) * (r - x_from_right))
            return area_total - segment_area
    
    # Бинарный поиск для нахождения x, соответствующего заданной площади
    def find_x(target_area):
        left, right = 0.0, d + 2 * r
        for _ in range(100):  # 100 итераций для высокой точности
            mid = (left + right) / 2.0
            current_area = area_to_x(mid)
            if current_area < target_area:
                left = mid
            else:
                right = mid
        return (left + right) / 2.0
    
    results = []
    for i in range(1, n):
        target_area = area_per_piece * i
        x = find_x(target_area)
        results.append("{:.6f}".format(x))
    
    with open('OUTPUT.TXT', 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == "__main__":
    main()
