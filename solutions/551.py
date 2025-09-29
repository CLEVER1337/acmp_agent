
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        R, r, h, b = map(int, f.readline().split())
    
    # Вычисляем максимальное расстояние от центра ограды до верхушки упавшего дерева
    # Дерево падает так, что образуется прямоугольный треугольник с катетами h и r
    # Расстояние от центра пня до верхушки упавшего дерева: sqrt(h^2 + r^2)
    max_distance_from_stump_center = math.sqrt(h**2 + r**2)
    
    # Расстояние от центра ограды до верхушки упавшего дерева в худшем случае
    # (когда дерево падает в направлении от центра ограды)
    max_distance_from_fence_center = b + max_distance_from_stump_center
    
    if max_distance_from_fence_center <= R:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
