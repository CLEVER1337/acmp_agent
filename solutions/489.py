
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); K = int(data[idx+1]); idx += 2
    
    initial_coins = list(map(int, data[idx:idx+N]))
    idx += N
    
    final_coins = list(map(int, data[idx:idx+N-1]))
    idx += N-1
    
    protocol = list(map(int, data[idx:idx+K]))
    idx += K
    
    initial_state = {}
    for coin in initial_coins:
        abs_coin = abs(coin)
        side = 1 if coin > 0 else -1
        initial_state[abs_coin] = initial_state.get(abs_coin, 0) + side
    
    final_state = {}
    for coin in final_coins:
        abs_coin = abs(coin)
        side = 1 if coin > 0 else -1
        final_state[abs_coin] = final_state.get(abs_coin, 0) + side
    
    protocol_count = {}
    for nominal in protocol:
        protocol_count[nominal] = protocol_count.get(nominal, 0) + 1
    
    all_nominals = set(initial_state.keys()) | set(final_state.keys()) | set(protocol_count.keys())
    
    for nominal in all_nominals:
        initial_side = initial_state.get(nominal, 0)
        final_side = final_state.get(nominal, 0)
        flips = protocol_count.get(nominal, 0)
        
        expected_final_side = initial_side * ((-1) ** flips)
        
        if expected_final_side != final_side:
            result = nominal if expected_final_side > 0 else -nominal
            print(result)
            return

if __name__ == "__main__":
    main()
