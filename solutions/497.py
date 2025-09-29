
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    K = int(data[1])
    
    # Количество сегментов для каждой цифры
    seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    # Проверка на невозможность
    min_seg = N * 2  # минимально возможное (все цифры 1)
    max_seg = N * 7  # максимально возможное (все цифры 8)
    if K < min_seg or K > max_seg:
        print("NO SOLUTION")
        return
    
    # Минимальное число
    min_num = [0] * N
    remaining = K
    
    # Сначала пытаемся поставить минимальные цифры слева направо
    for i in range(N):
        # Для первой цифры нельзя 0
        start_digit = 0 if i > 0 else 1
        for d in range(start_digit, 10):
            # Минимальное количество сегментов для оставшихся цифр
            min_rest = (N - i - 1) * 2
            # Максимальное количество сегментов для оставшихся цифр
            max_rest = (N - i - 1) * 7
            
            # Проверяем, можем ли поставить цифру d
            if seg[d] <= remaining and (remaining - seg[d]) >= min_rest and (remaining - seg[d]) <= max_rest:
                min_num[i] = d
                remaining -= seg[d]
                break
    
    # Максимальное число
    max_num = [0] * N
    remaining = K
    
    for i in range(N):
        # Для первой цифры нельзя 0
        start_digit = 9 if i == 0 else 9
        end_digit = 1 if i == 0 else 0
        step = -1
        
        for d in range(start_digit, end_digit - 1, step):
            # Минимальное количество сегментов для оставшихся цифр
            min_rest = (N - i - 1) * 2
            # Максимальное количество сегментов для оставшихся цифр
            max_rest = (N - i - 1) * 7
            
            # Проверяем, можем ли поставить цифру d
            if seg[d] <= remaining and (remaining - seg[d]) >= min_rest and (remaining - seg[d]) <= max_rest:
                max_num[i] = d
                remaining -= seg[d]
                break
    
    # Проверяем, что оба числа корректны
    if min_num[0] == 0 or max_num[0] == 0:
        print("NO SOLUTION")
        return
    
    # Выводим результаты
    print(''.join(map(str, min_num)))
    print(''.join(map(str, max_num)))

if __name__ == "__main__":
    main()
