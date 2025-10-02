
MOD = 10**9 + 7

def solve():
    c = input().strip()
    n = len(c)
    
    # Проверяем возможность представления в виде суммы n-значных чисел
    # Минимальное n-значное число: 10**(n-1)
    # Максимальное n-значное число: 10**n - 1
    min_val = 10**(n-1)
    max_val = 10**n - 1
    
    # Если C слишком большое или слишком маленькое
    if int(c) < 2 * min_val or int(c) > 2 * max_val:
        print(0)
        return
    
    # DP для подсчета количества красивых чисел длины n
    # dp[i][d] - количество красивых чисел длины i, оканчивающихся на цифру d
    dp = [[0] * 10 for _ in range(n+1)]
    
    # Инициализация для чисел длины 1
    for d in range(1, 10):
        dp[1][d] = 1
    
    # Заполняем DP для всех длин
    for i in range(2, n+1):
        for d in range(10):
            for prev_d in range(10):
                if d != prev_d:
                    dp[i][d] = (dp[i][d] + dp[i-1][prev_d]) % MOD
    
    # Общее количество красивых чисел длины n
    total_beautiful = sum(dp[n]) % MOD
    
    # Теперь считаем количество пар (A, B) где A + B = C
    # И оба числа красивые и n-значные
    
    # Для каждой позиции в разрядах
    # memo[i][carry][tight] - количество способов для первых i цифр
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def count_ways(pos, carry, tight_a, tight_b, last_a, last_b):
        if pos == n:
            if carry == 0 and not tight_a and not tight_b:
                return 1
            return 0
        
        total = 0
        digit_c = int(c[pos])
        
        # Перебираем возможные цифры для A и B
        for a_digit in range(10):
            if tight_a and a_digit > digit_c:
                continue
            if pos == 0 and a_digit == 0:
                continue
                
            for b_digit in range(10):
                if tight_b and b_digit > digit_c:
                    continue
                if pos == 0 and b_digit == 0:
                    continue
                
                # Проверяем красивость цифр
                if pos > 0:
                    if last_a is not None and a_digit == last_a:
                        continue
                    if last_b is not None and b_digit == last_b:
                        continue
                
                current_sum = a_digit + b_digit + carry
                new_carry = current_sum // 10
                current_digit = current_sum % 10
                
                if current_digit != digit_c:
                    continue
                
                new_tight_a = tight_a and (a_digit == digit_c)
                new_tight_b = tight_b and (b_digit == digit_c)
                
                total = (total + count_ways(pos+1, new_carry, new_tight_a, new_tight_b, a_digit, b_digit)) % MOD
        
        return total
    
    result = count_ways(0, 0, True, True, None, None)
    print(result % MOD)

solve()
