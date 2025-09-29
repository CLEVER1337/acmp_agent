
# Открываем файл INPUT.TXT для чтения
with open('INPUT.txt', 'r') as file:
    n = int(file.read())

# Преобразуем число в двоичную строку и подсчитываем единицы
binary_n = bin(n)[2:]  # [2:] убирает префикс '0b' из строки
count_of_ones = binary_n.count('1')

# Записываем результат в файл OUTPUT.TXT
with open('OUTPUT.txt', 'w') as file:
    file.write(str(count_of_ones))
