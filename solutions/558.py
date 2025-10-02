
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    radii = list(map(int, data[1:1+n]))
    
    radii.sort(reverse=True)
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                r1, r2, r3 = radii[i], radii[j], radii[k]
                
                # Проверяем, можно ли составить треугольник из трех касающихся кругов
                if r1 >= r2 + r3:
                    continue
                    
                # Вычисляем радиус вписанной окружности (круга Декарта)
                # Формула Декарта для трех касающихся кругов
                k1, k2, k3 = 1/r1, 1/r2, 1/r3
                k4 = k1 + k2 + k3 + 2 * math.sqrt(k1*k2 + k2*k3 + k3*k1)
                r4 = 1 / k4
                
                # Проверяем все меньшие круги
                for l in range(k+1, n):
                    if radii[l] <= r4:
                        count += 1
    
    print(count)

if __name__ == "__main__":
    main()
