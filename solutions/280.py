
def main():
    with open("INPUT.TXT", "r") as f:
        x = int(f.read().strip())
    
    if x == 1:
        with open("OUTPUT.TXT", "w") as f:
            f.write("1")
        return
    
    # Факторизуем число x (по условию простые делители ≤ 1000)
    factors = {}
    temp = x
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    
    # Получаем список простых делителей
    primes = list(factors.keys())
    
    # Любой делитель, делящийся на все простые делители x, имеет вид:
    # y = p1^a1 * p2^a2 * ... * pk^ak * m, где 0 <= ai <= factors[pi]
    # и m - любое число, взаимно простое с x
    
    # Количество возможных значений для каждого простого множителя
    count = 1
    for p in primes:
        count *= (factors[p] + 1)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
