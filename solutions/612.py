
def solve(X, Y):
    if len(Y) > len(X): return "Impossible"
    
    Z = 'A' * len(Y)  # Создаем пустое слово Z и добавляем к нему букву 'A', столько раз, сколько длина Y.

    while len(Z) < len(X):   # Пока длина Z меньше X, добавляем в конец слова 'A' и затем перед ним 'B'.
        Z += 'A' + 'B' * (len(Y)-1) if len(Z) % 2 == 0 else 'B' + 'A' * (len(Y)-1)
        
    return Z[:len(X)]   # Возвращаем результирующее слово.

if __name__ == "__main__":
    with open("INPUT.TXT", "r") as file:  # Открываем файл для чтения.
        X = file.readline().strip()   # Считываем первую строку из файла.
        Y = file.readline().strip()   # Считываем вторую строку из файла.
        
    result = solve(X, Y)  # Решаем задачу.
    
    with open("OUTPUT.TXT", "w") as file:  # Открываем файл для записи.
        file.write(result + '\n')   # Записываем результат в файл.
