
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    for k in range(1, N + 1):
        for v in range(1, N + 1):
            p = N - k - v
            if p <= 0:
                continue
            
            # Имитация процесса
            # Шаг 1: Петя дает Васе и Коле по столько, сколько у них было
            p1 = p - v - k
            v1 = v + v
            k1 = k + k
            
            # Шаг 2: Коля дает Васе и Пете по столько, сколько у них стало
            k2 = k1 - v1 - p1
            v2 = v1 + v1
            p2 = p1 + p1
            
            # Шаг 3: Вася дает Пете и Коле по столько, сколько у них стало
            v3 = v2 - p2 - k2
            p3 = p2 + p2
            k3 = k2 + k2
            
            # Проверяем, что у всех поровну
            if p3 == v3 == k3 and p3 + v3 + k3 == N:
                with open('OUTPUT.TXT', 'w') as f:
                    f.write(f"{p} {v} {k}")
                return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("0 0 0")

if __name__ == "__main__":
    main()
