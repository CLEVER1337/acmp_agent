
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("No solution")
        return
        
    n = int(data[0])
    f = list(map(int, data[1:5]))
    
    # Функция f представлена как [f(0,0), f(0,1), f(1,0), f(1,1)]
    
    # Если f(0,0)=1, то можно использовать все нули
    if f[0] == 1:
        print('0' * n)
        return
        
    # Если f(1,1)=1, то можно использовать все единицы
    if f[3] == 1:
        print('1' * n)
        return
        
    # Если f(0,1)=1 и f(1,0)=1, то можно чередовать 0 и 1
    if f[1] == 1 and f[2] == 1:
        # Максимальное количество единиц: чередование начинается с 1
        result = []
        for i in range(n):
            result.append('1' if i % 2 == 0 else '0')
        print(''.join(result))
        return
        
    # Если f(0,1)=1, то можно использовать один 0 в начале и остальные единицы
    if f[1] == 1:
        if n >= 2:
            print('0' + '1' * (n - 1))
            return
        else:
            print("No solution")
            return
            
    # Если f(1,0)=1, то можно использовать один 0 в конце и остальные единицы
    if f[2] == 1:
        if n >= 2:
            print('1' * (n - 1) + '0')
            return
        else:
            print("No solution")
            return
            
    # Во всех остальных случаях решения нет
    print("No solution")

if __name__ == "__main__":
    main()
