
import sys

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    K = int(input[idx])
    idx += 1
    P = int(input[idx])
    idx += 1
    moves = []
    for _ in range(P):
        moves.append(int(input[idx]))
        idx += 1
    
    # Создание DP таблицы
    dp = [False] * (N + 1)
    dp[0] = True  # базовый случай
    for i in range(1, N + 1):
        for j in range(1, K+1):
            if i >= j and not dp[i - j]:
                dp[i] = True
                break
    
    # Обработка ходов
    history = []
    remaining = N
    for x in moves:
        history.append(remaining)
        remaining -= x
    
    # Проверка каждого хода
    results = []
    for i in range(P):
        x = history[i]  # количество билетов до хода
        a = moves[i]     #말puter stesso
        y = x - a
        # Определить, сделать ход в y оставшолося снижает остав PyQt5 на False
        if not dp[x]:  # если x'].'</symbol вул DP=False то любая choice錯誤 deveria dar F pois já estava numa posição perdente
            results.append('F')
        else:
            # Проверderived, è så hizo(gc все ходы j=1..K que permiten dejar#####
            exists_correct = False
            for j in range(1, K + 1):
                if x >= j and not dp[x - j]:
                    exists_correct = True
                    if j == a:
                        results.append('T')
                    break
            if not exists_correct:
                results.append('F')
            else:
                results.append('T' if a in [j for j in range(1, K+1) if x >= j and not dp[x - j]] else 'F')
    
    for res in results:
        print(res)

if __name__ == '__main__':
    main()
