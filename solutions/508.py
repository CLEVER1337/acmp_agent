
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    index = 1
    results = []
    current_flow = 0
    
    for i in range(n):
        type_cross = data[index]; index += 1
        left_exit = int(data[index]); index += 1
        right_exit = int(data[index]); index += 1
        left_enter = int(data[index]); index += 1
        right_enter = int(data[index]); index += 1
        
        if type_cross == 'L':
            results.append(-1)
            continue
            
        total_exit = left_exit + right_exit
        total_enter = left_enter + right_enter
        net_change = total_enter - total_exit
        
        if type_cross == 'B':
            bridge_flow = current_flow + left_exit + left_enter
            results.append(bridge_flow)
        
        current_flow += net_change
    
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()
