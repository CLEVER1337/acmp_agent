
def main():
    n = int(input().strip())
    for a in range(1, n):
        for b in range(1, n):
            c = n - a - b
            if c <= 0:
                continue
                
            # Шаг 1: Петя дает Васе и Коле по столько, сколько у них есть
            p1 = a - b - c
            v1 = b + b
            k1 = c + c
            
            # Шаг 2: Коля дает Васе и Пете по столько, сколько у них стало
            p2 = p1 + p1
            v2 = v1 + v1
            k2 = k1 - p1 - v1
            
            # Шаг 3: Вася дает Пете и Коле по столько, сколько у них стало
            p3 = p2 + p2
            v3 = v2 - p2 - k2
            k3 = k2 + k2
            
            if p3 == v3 == k3 and p3 > 0:
                print(a, b, c)
                return

if __name__ == "__main__":
    main()
