
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = list(map(float, f.readline().split()))
    
    x1, y1, x2, y2, xc, yc, r = data
    
    # Вектор от центра круга к начальной точке
    dx1 = x1 - xc
    dy1 = y1 - yc
    dist1 = math.sqrt(dx1*dx1 + dy1*dy1)
    
    # Вектор от центра круга к конечной точке
    dx2 = x2 - xc
    dy2 = y2 - yc
    dist2 = math.sqrt(dx2*dx2 + dy2*dy2)
    
    # Проверяем, пересекает ли прямая круг
    # Уравнение прямой через точки (x1,y1) и (x2,y2)
    A = y2 - y1
    B = x1 - x2
    C = x2*y1 - x1*y2
    
    # Расстояние от центра круга до прямой
    dist_to_line = abs(A*xc + B*yc + C) / math.sqrt(A*A + B*B)
    
    # Если прямая не пересекает круг или касается его
    if dist_to_line >= r:
        # Идем по прямой
        path_length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    else:
        # Проверяем, находятся ли точки по одну сторону от касательных
        # Вектор от начальной точки к конечной
        dx = x2 - x1
        dy = y2 - y1
        
        # Вектор от начальной точки к центру круга
        dxc1 = xc - x1
        dyc1 = yc - y1
        
        # Вектор от конечной точки к центру круга
        dxc2 = xc - x2
        dyc2 = yc - y2
        
        # Угол между векторами
        dot1 = dx*dxc1 + dy*dyc1
        dot2 = (-dx)*dxc2 + (-dy)*dyc2
        
        # Если обе точки находятся за пределами касательных
        if dot1 > 0 and dot2 > 0:
            # Находим точки касания
            # Угол между касательными
            angle1 = math.acos(r/dist1)
            angle2 = math.acos(r/dist2)
            
            # Угол между векторами к точкам
            cos_angle = (dx1*dx2 + dy1*dy2) / (dist1*dist2)
            angle_between = math.acos(max(-1.0, min(1.0, cos_angle)))
            
            # Угол обхода
            tangent_angle = angle_between - angle1 - angle2
            
            # Длина пути по касательным
            tangent_length1 = math.sqrt(dist1*dist1 - r*r)
            tangent_length2 = math.sqrt(dist2*dist2 - r*r)
            
            # Длина дуги
            arc_length = r * tangent_angle
            
            path_length = tangent_length1 + tangent_length2 + arc_length
        else:
            # Идем по прямой
            path_length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.3f}".format(path_length))

if __name__ == "__main__":
    main()
