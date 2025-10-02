
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    results = []
    current_flow = 0
    
    for i in range(1, n + 1):
        parts = data[i].split()
        cross_type = parts[0]
        left_exit = int(parts[1])
        right_exit = int(parts[2])
        left_enter = int(parts[3])
        right_enter = int(parts[4])
        
        if cross_type == 'L':
            results.append(-1)
            current_flow += (left_enter + right_enter) - (left_exit + right_exit)
        else:
            bridge_flow = current_flow + left_enter - right_exit
            results.append(bridge_flow)
            current_flow += (left_enter + right_enter) - (left_exit + right_exit)
            
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()
