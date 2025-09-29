
def main():
    with open('INPUT.TXT', 'r') as f:
        W, H, x, y, a, b = map(int, f.readline().split())
    
    # Переводим размеры карты из см в метры
    a_meters = a / 100.0
    b_meters = b / 100.0
    
    # Коэффициенты сжатия для системы уравнений
    kx = a_meters / (2 * W)
    ky = b_meters / (2 * H)
    
    # Решаем систему уравнений:
    # u = kx * (u - x) + x
    # v = ky * (v - y) + y
    
    # Преобразуем к виду:
    # u * (1 - kx) = x * (1 - kx)
    # v * (1 - ky) = y * (1 - ky)
    
    u = x
    v = y
    
    print("{:.6f} {:.6f}".format(u, v))

if __name__ == "__main__":
    main()
