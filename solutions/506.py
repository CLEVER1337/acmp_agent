
import sys
from decimal import Decimal, getcontext

def main():
    data = sys.stdin.readline().split()
    N = int(data[0])
    K1 = int(data[1])
    K2 = int(data[2])
    S = Decimal(data[3])
    
    getcontext().prec = 10000
    
    dp = {}
    for i in range(N, -1, -1):
        for j in range(N, -1, -1):
            if i == N or j == N:
                dp[(i, j)] = Decimal(1) if i == N else Decimal(0)
            else:
                dp[(i, j)] = (dp[(i+1, j)] + dp[(i, j+1)]) / Decimal(2)
    
    petya_prob = dp[(K1, K2)]
    petya_coins = (petya_prob * S).to_integral_value(rounding='ROUND_HALF_UP')
    vasya_coins = S - petya_coins
    
    print(f"{petya_coins} {vasya_coins}")

if __name__ == "__main__":
    main()
