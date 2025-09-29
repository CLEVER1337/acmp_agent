
import math

def is_perfect_square(n):
    root = math.isqrt(n)
    return root * root == n

def main():
    with open('INPUT.TXT', 'r') as f:
        num = int(f.read().strip())
    
    if num < 1:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0\n')
        return
    
    # Проверка по формуле Бине: n является числом Фибоначчи если:
    # 5*n² + 4 или 5*n² - 4 является полным квадратом
    check1 = 5 * num * num + 4
    check2 = 5 * num * num - 4
    
    if is_perfect_square(check1) or is_perfect_square(check2):
        # Находим порядковый номер через формулу Бине
        phi = (1 + math.sqrt(5)) / 2
        if num == 1:
            # Особый случай для числа 1 (может быть 1-м или 2-м)
            with open('OUTPUT.TXT', 'w') as f:
                f.write('1\n1\n')
            return
            
        n = round(math.log(num * math.sqrt(5)) / math.log(phi))
        # Проверяем, что получили правильное число
        fib_n = round((phi**n - (-phi)**(-n)) / math.sqrt(5))
        if fib_n == num:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(f'1\n{n}\n')
        else:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('0\n')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0\n')

if __name__ == '__main__':
    main()
