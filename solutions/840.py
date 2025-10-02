
import math

def read_input():
    with open('INPUT.TXT', 'r') as f:
        data = f.readlines()
    
    center_x, center_y, center_z, radius = map(float, data[0].split())
    n = int(data[1])
    balls = []
    
    for i in range(2, 2 + n):
        x, y, z, r = map(float, data[i].split())
        balls.append((x, y, z, r))
    
    return (center_x, center_y, center_z, radius), n, balls

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def balls_intersect(x1, y1, z1, r1, x2, y2, z2, r2):
    dist = distance(x1, y1, z1, x2, y2, z2)
    return dist <= r1 + r2

def main():
    original_ball, n, balls = read_input()
    ox, oy, oz, orad = original_ball
    
    # Создаем список всех шаров (оригинальный + добавляемые)
    all_balls = [original_ball]
    ball_indices = [0]  # индекс 0 для оригинального шара
    
    for i in range(n):
        x, y, z, r = balls[i]
        all_balls.append((x, y, z, r))
        ball_indices.append(i + 1)
    
    # Проверяем, пересекается ли каждый шар хотя бы с одним другим
    isolated_balls = set(range(len(all_balls)))
    
    for i in range(len(all_balls)):
        for j in range(i + 1, len(all_balls)):
            x1, y1, z1, r1 = all_balls[i]
            x2, y2, z2, r2 = all_balls[j]
            
            if balls_intersect(x1, y1, z1, r1, x2, y2, z2, r2):
                if i in isolated_balls:
                    isolated_balls.remove(i)
                if j in isolated_balls:
                    isolated_balls.remove(j)
    
    # Если есть изолированные шары после добавления всех
    if isolated_balls:
        return 0
    
    # Постепенно добавляем шары и проверяем наличие изолированных
    current_balls = [original_ball]
    current_indices = [0]
    
    for i in range(n):
        x, y, z, r = balls[i]
        current_balls.append((x, y, z, r))
        current_indices.append(i + 1)
        
        # Проверяем наличие изолированных шаров
        isolated = set(range(len(current_balls)))
        
        for j in range(len(current_balls)):
            for k in range(j + 1, len(current_balls)):
                x1, y1, z1, r1 = current_balls[j]
                x2, y2, z2, r2 = current_balls[k]
                
                if balls_intersect(x1, y1, z1, r1, x2, y2, z2, r2):
                    if j in isolated:
                        isolated.remove(j)
                    if k in isolated:
                        isolated.remove(k)
        
        # Если нет изолированных шаров
        if not isolated:
            return i + 1
    
    return 0

if __name__ == "__main__":
    result = main()
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))
