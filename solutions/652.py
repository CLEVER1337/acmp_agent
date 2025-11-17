
from collections import deque

def quantum_computer(N, K):
    # Создаем начальный массив из N элементов от 1 до N
    array = list(range(1, N+1))
    
    # Читаем операции из входного файла
    with open('INPUT.TXT', 'r') as f:
        operations = deque([line.strip().split() for line in f.readlines()[1:]])
        
    # Обрабатываем операции по очереди
    while operations:
        operation, L, R = operations.popleft()
        L, R = int(L), int(R)
        
        if operation == 'I':
            # Инвертируем части массива
            array[L-1:R] = array[L-1:R][::-1]
            
        elif operation == 'S':
            # Выводим сумму элементов массива
            print(sum(array[L-1:R]))

if __name__ == "__main__":
    N, K =  map(int, input().split())
    quantum_computer(N, K)
