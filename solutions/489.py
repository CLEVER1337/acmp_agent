
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    initial_coins = list(map(int, data[2:2+n]))
    final_coins = list(map(int, data[2+n:2+n+n-1]))
    protocol = list(map(int, data[2+n+n-1:2+n+n-1+k]))
    
    initial_count = {}
    for coin in initial_coins:
        abs_coin = abs(coin)
        sign = -1 if coin < 0 else 1
        initial_count[abs_coin] = initial_count.get(abs_coin, 0) + sign
    
    final_count = {}
    for coin in final_coins:
        abs_coin = abs(coin)
        sign = -1 if coin < 0 else 1
        final_count[abs_coin] = final_count.get(abs_coin, 0) + sign
    
    flip_count = {}
    for coin_val in protocol:
        flip_count[coin_val] = flip_count.get(coin_val, 0) + 1
    
    possible_coins = {}
    for coin_val in set(initial_count.keys()) | set(final_count.keys()) | set(flip_count.keys()):
        initial_sign = initial_count.get(coin_val, 0)
        final_sign = final_count.get(coin_val, 0)
        flips = flip_count.get(coin_val, 0)
        
        expected_final_sign = initial_sign
        if flips % 2 == 1:
            expected_final_sign = -expected_final_sign
        
        if expected_final_sign != final_sign:
            diff = abs(expected_final_sign - final_sign)
            if diff == 2:
                possible_coins[coin_val] = expected_final_sign
    
    if len(possible_coins) == 1:
        coin_val, sign = next(iter(possible_coins.items()))
        result = -coin_val if sign == -1 else coin_val
        print(result)
    else:
        for coin_val in possible_coins:
            if possible_coins[coin_val] == 1:
                print(coin_val)
                return
        print(-coin_val)

if __name__ == "__main__":
    main()
