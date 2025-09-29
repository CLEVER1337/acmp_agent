
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    bounds = []
    index = 1
    for i in range(n):
        l = data[index]
        r = data[index+1]
        index += 2
        bounds.append((l, r))
    
    # Создаем массив для хранения значений переменных циклов
    var_values = [0] * (n + 1)
    
    # Обрабатываем циклы от внешнего к внутреннему
    for i in range(n):
        l_str, r_str = bounds[i]
        
        # Определяем левую границу
        if l_str.startswith('-'):
            # Используем значение переменной предыдущего цикла
            var_idx = int(l_str[1:])
            left = var_values[var_idx]
        else:
            left = int(l_str)
        
        # Определяем правую границу
        right = int(r_str)
        
        # Если левая граница больше правой, цикл не выполняется
        if left > right:
            var_values[i + 1] = 0
        else:
            var_values[i + 1] = right - left + 1
    
    # Результат - значение самого внутреннего цикла
    result = var_values[n]
    print(result)

if __name__ == "__main__":
    main()
