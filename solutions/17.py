import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    sequence = list(map(int, data[1:1+n]))
    
    # Находим все делители (n-1)
    divisors = []
    for i in range(1, n + 1):
        if (n - 1) % i == 0:
            divisors.append(i)
    
    # Проверяем делители от наименьшего к наибольшему
    for k in divisors:
        valid = True
        # Проверяем периодичность для первых n-1 элементов
        for i in range(n - 1):
            if sequence[i] != sequence[i % k]:
                valid = False
                break
        # Проверяем, что последний равен первому
        if sequence[n-1] != sequence[0]:
            valid = False
            
        if valid:
            print(k)
            return

if __name__ == "__main__":
    main()
