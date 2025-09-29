
import math

def main():
    with open("INPUT.TXT", "r") as f:
        n, k = map(int, f.readline().split())
    
    if k > n:
        print(0)
        return
    
    # Выбираем k позиций для неподвижных точек
    fixed_points_comb = math.comb(n, k)
    
    # Для остальных n-k элементов нужно, чтобы ни один не был на своем месте
    # Это задача о беспорядках (derangements)
    m = n - k
    derangements = 0
    for i in range(m + 1):
        sign = 1 if i % 2 == 0 else -1
        derangements += sign * math.comb(m, i) * math.factorial(m - i)
    
    result = fixed_points_comb * derangements
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
