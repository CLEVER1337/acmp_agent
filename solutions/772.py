
def main():
    import sys
    data = sys.stdin.readline().split()
    n = int(data[0])
    m = int(data[1])
    bends = data[2:2+m]
    
    layers = []
    for i in range(n + 1):
        layers.append((i, 'F'))
    
    for bend in bends:
        idx = int(bend[:-1])
        direction = bend[-1]
        
        if idx > len(layers) - 1:
            print("SCRUFFY")
            return
            
        left_part = layers[:idx]
        right_part = layers[idx:]
        
        if direction == 'F':
            right_part = [(num, 'R' if side == 'F' else 'F') for num, side in reversed(right_part)]
        else:
            right_part = [(num, 'F' if side == 'R' else 'R') for num, side in reversed(right_part)]
            
        layers = left_part + right_part
        
        if len(layers) != n + 1:
            print("SCRUFFY")
            return
            
    result_F = []
    result_R = []
    
    for num, side in layers:
        if side == 'F':
            result_F.append(f"P{num}F")
        else:
            result_R.append(f"P{num}R")
            
    result = result_F + result_R
    print(" ".join(result))

if __name__ == "__main__":
    main()
