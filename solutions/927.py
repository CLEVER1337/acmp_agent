
MOD = 10**9 + 7

def solve():
    s = input().strip()
    n = len(s)
    
    # Динамическое программирование для подсчета красивых чисел длины n
    # dp[i][d] - количество красивых чисел длины i, оканчивающихся на цифру d
    dp = [[0] * 10 for _ in range(n + 1)]
    
    # Инициализация для чисел длины 1 (не могут начинаться с 0)
    for d in range(1, 10):
        dp[1][d] = 1
    
    # Заполнение DP для красивых чисел
    for i in range(2, n + 1):
        for d in range(10):
            for prev_d in range(10):
                if d != prev_d:
                    dp[i][d] = (dp[i][d] + dp[i - 1][prev_d]) % MOD
    
    # Общее количество красивых чисел длины n
    total_beautiful = sum(dp[n]) % MOD
    
    # Теперь считаем количество пар (A, B) где A + B = C
    # И A, B - красивые числа длины n
    
    # Для каждой позиции цифры в числе C
    # dp2[i][carry][d] - количество способов для первых i цифр с переносом carry,
    # где последняя цифра A была d
    dp2 = [[[0] * 10 for _ in range(2)] for __ in range(n + 1)]
    
    # Инициализация: начинаем с младшего разряда (i=0), перенос 0
    dp2[0][0][0] = 1
    
    for i in range(n):
        digit_c = int(s[n - 1 - i])  # цифра C с конца
        for carry in range(2):
            for last_d_a in range(10):
                if dp2[i][carry][last_d_a] == 0:
                    continue
                
                # Перебираем цифру a для текущего разряда числа A
                for a_digit in range(10):
                    if i == n - 1 and a_digit == 0:  # первая цифра не может быть 0
                        continue
                    
                    # Цифра b = (c - a - carry + 10) % 10, новый перенос = (a + b + carry) // 10
                    total = a_digit + carry
                    b_digit = (digit_c - total % 10 + 10) % 10
                    new_carry = (total + b_digit) // 10
                    
                    if new_carry > 1:  # перенос не может быть больше 1
                        continue
                    
                    # Проверяем, что цифра A красивая (не совпадает с предыдущей)
                    if i > 0 and a_digit == last_d_a:
                        continue
                    
                    # Проверяем, что B - корректное число (первая цифра не 0)
                    if i == n - 1 and b_digit == 0:
                        continue
                    
                    # Обновляем DP
                    dp2[i + 1][new_carry][a_digit] = (
                        dp2[i + 1][new_carry][a_digit] + dp2[i][carry][last_d_a]
                    ) % MOD
    
    # Суммируем все способы для всего числа
    result = 0
    for carry in range(2):
        for last_d in range(10):
            result = (result + dp2[n][carry][last_d]) % MOD
    
    print(result)

solve()
