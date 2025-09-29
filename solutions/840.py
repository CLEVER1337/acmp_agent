
import math

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Читаем исходный шар
    x, y, z, r = map(float, lines[0].split())
    original_ball = (x, y, z, r)
    
    # Читаем количество добавляемых шаров
    n = int(lines[1].strip())
    
    # Читаем добавляемые шары
    balls = []
    for i in range(2, 2 + n):
        xi, yi, zi, ri = map(float, lines[i].split())
        balls.append((xi, yi, zi, ri))
    
    return original_ball, balls

def distance_between_centers(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def balls_intersect(ball1, ball2):
    x1, y1, z1, r1 = ball1
    x2, y2, z2, r2 = ball2
    distance = distance_between_centers(x1, y1, z1, x2, y2, z2)
    return distance <= (r1 + r2)

def main():
    original_ball, balls = read_input('INPUT.TXT')
    all_balls = [original_ball]
    
    for i, ball in enumerate(balls, 1):
        all_balls.append(ball)
        
        # Проверяем, есть ли хотя бы один шар, не пересекающийся с другими
        has_isolated = False
        for j, current_ball in enumerate(all_balls):
            intersects_with_any = False
            for k, other_ball in enumerate(all_balls):
                if j != k and balls_intersect(current_ball, other_ball):
                    intersects_with_any = True
                    break
            
            if not intersects_with_any:
                has_isolated = True
                break
        
        # Если нет изолированных шаров, можно остановиться
        if not has_isolated:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(str(i))
            return
    
    # Если после всех добавлений все еще есть изолированные шары
    with open('OUTPUT.TXT', 'w') as f:
        f.write('0')

if __name__ == '__main__':
    main()
