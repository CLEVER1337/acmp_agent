
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    rates = []
    index = 1
    for i in range(n):
        dollar = float(data[index])
        euro = float(data[index + 1])
        index += 2
        rates.append((dollar, euro))
    
    rubles = 100.0
    dollars = 0.0
    euros = 0.0
    
    for i in range(n):
        dollar_rate, euro_rate = rates[i]
        
        # Рассчитываем максимальное количество рублей, которое можно получить
        # из имеющихся валют в текущий день
        current_rubles = rubles
        if dollars > 0:
            current_rubles = max(current_rubles, dollars * dollar_rate)
        if euros > 0:
            current_rubles = max(current_rubles, euros * euro_rate)
        
        # Обновляем состояние для следующего дня
        # Мы можем держать деньги в рублях, долларах или евро
        next_rubles = current_rubles
        next_dollars = current_rubles / dollar_rate if dollar_rate > 0 else 0
        next_euros = current_rubles / euro_rate if euro_rate > 0 else 0
        
        # Также учитываем возможность конвертации между валютами
        # Доллары через евро
        if dollars > 0 and euro_rate > 0:
            via_euro = dollars * dollar_rate / euro_rate
            next_euros = max(next_euros, via_euro)
        
        # Евро через доллары
        if euros > 0 and dollar_rate > 0:
            via_dollar = euros * euro_rate / dollar_rate
            next_dollars = max(next_dollars, via_dollar)
        
        rubles = next_rubles
        dollars = next_dollars
        euros = next_euros
    
    print("{:.2f}".format(rubles))

if __name__ == "__main__":
    main()
