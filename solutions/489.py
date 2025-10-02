
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    initial_coins = list(map(int, data[2:2+n]))
    final_coins = list(map(int, data[2+n:2+n+n-1]))
    protocol = list(map(int, data[2+n+n-1:2+n+n-1+k]))
    
    initial_state = {}
    for coin in initial_coins:
        nominal = abs(coin)
        side = 1 if coin < 0 else 0
        initial_state[nominal] = initial_state.get(nominal, 0) + (1 if side == 1 else 0)
    
    final_state = {}
    for coin in final_coins:
        nominal = abs(coin)
        side = 1 if coin < 0 else 0
        final_state[nominal] = final_state.get(nominal, 0) + (1 if side == 1 else 0)
    
    flip_count = {}
    for nominal in protocol:
        flip_count[nominal] = flip_count.get(nominal, 0) + 1
    
    all_nominals = set(initial_state.keys()) | set(final_state.keys()) | set(flip_count.keys())
    
    for nominal in all_nominals:
        initial_heads = initial_state.get(nominal, 0)
        final_heads = final_state.get(nominal, 0)
        flips = flip_count.get(nominal, 0)
        
        expected_final_heads = (initial_heads + flips) % 2
        
        if nominal not in final_state:
            if expected_final_heads == 0:
                print(nominal)
            else:
                print(-nominal)
            return
        
        if expected_final_heads != final_heads:
            if expected_final_heads == 0:
                print(nominal)
            else:
                print(-nominal)
            return

if __name__ == "__main__":
    main()
