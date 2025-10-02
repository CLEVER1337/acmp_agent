
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        K = int(data[0])
        p1 = int(data[1]) / 100.0
        p2 = int(data[2]) / 100.0
        p3 = int(data[3]) / 100.0

    # Математическое ожидание очков для каждой провинции
    # E_старшая = x*(p1 + p3*0.5) + (K-x)*(1-p2)
    # E_младшая = x*(1-p1-p3 + p3*0.5) + (K-x)*p2
    
    # Разность: E_старшая - E_младшая = x*(p1 + p3*0.5 - (1-p1-p3 + p3*0.5)) + (K-x)*(1-p2 - p2)
    # = x*(2*p1 + p3 - 1) + (K-x)*(1-2*p2)
    
    # Упрощаем: diff = x*(2*p1 + p3 - 1 - (1-2*p2)) + K*(1-2*p2)
    # = x*(2*p1 + p3 - 1 - 1 + 2*p2) + K*(1-2*p2)
    # = x*(2*p1 + p3 + 2*p2 - 2) + K*(1-2*p2)
    
    # Коэффициент при x: A = 2*p1 + p3 + 2*p2 - 2
    
    A = 2 * p1 + p3 + 2 * p2 - 2
    
    if abs(A) < 1e-12:
        # Любое количество шахматных партий дает одинаковую разность
        result = 0
    else:
        # Ищем x, минимизирующий |A*x + C|, где C = K*(1-2*p2)
        C = K * (1 - 2 * p2)
        
        # Оптимальное x = -C/A (если в пределах [0, K])
        x_opt = -C / A
        
        # Проверяем границы
        candidates = []
        candidates.append(max(0, min(K, round(x_opt))))
        candidates.append(max(0, min(K, int(x_opt))))
        candidates.append(max(0, min(K, int(x_opt) + 1)))
        
        # Находим кандидата с минимальной абсолютной разностью
        min_diff = float('inf')
        best_x = 0
        for x_candidate in candidates:
            diff_val = abs(A * x_candidate + C)
            if diff_val < min_diff - 1e-12:
                min_diff = diff_val
                best_x = x_candidate
        
        result = best_x

    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
