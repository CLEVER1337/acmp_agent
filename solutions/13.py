
def bulls_and_cows(secret, guess):
    secret = str(secret)
    guess = str(guess)
    
    bulls = 0
    cows = 0
    
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
            
    return bulls, cows

# Чтение входных данных из файла INPUT.TXT
with open('INPUT.txt', 'r') as file:
    secret, guess = map(int, file.readline().split())
    
bulls, cows = bulls_and_cows(secret, guess)

# Запись результата в файл OUTPUT.TXT
with open('OUTPUT.txt', 'w') as file:
    file.write(f'{bulls} {cows}\n')
