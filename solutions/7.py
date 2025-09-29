
# Открываем файл для чтения
with open('INPUT.TXT', 'r') as file:
    # Считываем строку и разделяем ее на три числа
    a, b, c = map(int, file.read().split())

# Находим максимальное из трёх чисел
max_coins = max(a, b, c)

# Открываем файл для записи и записываем результат
with open('OUTPUT.TXT', 'w') as file:
    file.write(str(max_coins))
