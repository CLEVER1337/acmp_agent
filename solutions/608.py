
def check_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    """Проверяет пересечение отрезков (x1,y1)-(x2,y2) и (x3,y3)-(x4,y4)."""
    
    def orientation(p, q, r):
        """Определяет ориентацию точки p относительно отрезка qr."""
        
        val = (q[1] - r[1]) * (p[0] - r[0]) + (r[0] - q[0]) * (p[1] - r[1])
        if val == 0: return 0 # p лежит на отрезке qr
        elif val < 0: return 2 # p поворот влево относительно qr
        else: return 1 # p поворот вправо относительно qr
    
    o1 = orientation(x1, y1, x2, y2, x3)
    o2 = orientation(x1, y1, x2, y2, x4)
    o3 = orientation(x3, y3, x4, y4, x1)
    o4 = orientation(x3, y3, x4, y4, x2)
    
    return (o1 != o2) and (o3 != o4) # если ориентации противоположны - отрезки пересекаются

def main():
    with open('INPUT.TXT', 'r') as f:
        mashka = tuple(map(int, next(f).split())) # координаты Машки
        lenka = tuple(map(int, next(f).split()))  # координаты Ленки
        n = int(next(f))                            # число препятствий
        
    for _ in range(n):
        obstacle = tuple(map(int, next(f).split())) # координаты препятствия
        
        if check_intersection(*mashka, *lenka, *obstacle):
            print('NO')
            return
    
    print('YES')
    print(f'{(mashka[0] + lenka[0]) / 2} {(mashka[1] + lenka[1]) / 2}') # средние координаты Машки и Ленки

if __name__ == '__main__':
    main()
