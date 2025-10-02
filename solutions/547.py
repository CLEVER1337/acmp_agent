
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    # Убираем множители 2 и 5 из n
    temp_n = n
    preperiod_length = 0
    while temp_n % 2 == 0:
        temp_n //= 2
        preperiod_length += 1
    while temp_n % 5 == 0:
        temp_n //= 5
        preperiod_length += 1
    
    # Если после удаления 2 и 5 осталась 1, то период = 0
    if temp_n == 1:
        period_length = 0
    else:
        # Находим длину периода для несократимой дроби
        # Период равен порядку 10 по модулю temp_n
        period_length = 1
        remainder = 10 % temp_n
        while remainder != 1:
            period_length += 1
            remainder = (remainder * 10) % temp_n
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{preperiod_length} {period_length}")

if __name__ == "__main__":
    main()
